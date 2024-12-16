import time
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("automation_check.log")
    ]
)

def log_step(message):
    logging.info(message)

# Настройка Chrome WebDriver
log_step("Настраиваем Chrome WebDriver...")
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")  # Опционально: запуск в фоновом режиме
options.add_argument("--disable-blink-features=AutomationControlled")  # Скрытие флага автоматизации

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # URL для проверки
    url = "https://bot.sannysoft.com/"
    log_step(f"Открываем сайт для проверки автоматизации: {url}")
    driver.get(url)

    # Ждем полной загрузки страницы
    log_step("Ждем полной загрузки страницы (до 30 секунд)...")
    WebDriverWait(driver, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # Пауза для выполнения скриптов
    log_step("Пауза на 5 секунд для выполнения всех скриптов...")
    time.sleep(5)

    # Получаем HTML-контент страницы
    log_step("Получаем HTML-контент страницы...")
    page_source = driver.page_source

    # Проверяем наличие флагов, указывающих на автоматизацию
    automation_indicators = [
        "webdriver", "HeadlessChrome", "bot", "automation", "selenium"
    ]
    detected_flags = [flag for flag in automation_indicators if flag.lower() in page_source.lower()]

    if detected_flags:
        log_step(f"Автоматизация распознана! Найдены флаги: {', '.join(detected_flags)}")
    else:
        log_step("Автоматизация не распознана. Все чисто.")

    # Делаем скриншот
    screenshot_path = "automation_check_screenshot.png"
    log_step(f"Делаем скриншот страницы и сохраняем как '{screenshot_path}'")
    driver.save_screenshot(screenshot_path)

    log_step("Скрипт выполнен успешно. Проверьте скриншот и лог файл.")

except Exception as e:
    logging.error(f"Произошла ошибка: {e}")

finally:
    log_step("Закрываем браузер.")
    driver.quit()