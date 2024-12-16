import time
import logging
import undetected_chromedriver as uc
from bs4 import BeautifulSoup  # For parsing HTML content / Для парсинга HTML-контента

# Настройка логирования / Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console / Логи в консоль
        logging.FileHandler("automation_check.log")  # Log to file / Логи в файл
    ]
)

def log_step(message):
    logging.info(message)  # Function for logging steps / Функция для логирования шагов

driver = None  # Declare driver globally / Глобальное объявление драйвера

try:
    # Настройка undetected_chromedriver / Setting up undetected_chromedriver
    log_step("Setting up undetected_chromedriver... / Настраиваем undetected_chromedriver...")
    options = uc.ChromeOptions()
    options.add_argument("--window-size=1920,1080")  # Set browser window size / Размер окна браузера
    options.add_argument("--disable-blink-features=AutomationControlled")  # Hide automation flags / Скрываем признаки автоматизации
    options.headless = False  # Run browser in visible mode / Запуск в видимом режиме

    driver = uc.Chrome(options=options)  # Launch browser / Запускаем браузер

    # Маскировка navigator.webdriver / Remove navigator.webdriver flag
    log_step("Removing 'navigator.webdriver' flag... / Удаляем флаг 'navigator.webdriver'...")
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        """
    })

    # Открываем сайт Intoli / Open the Intoli test website
    url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
    log_step(f"Opening website: {url} / Открываем сайт: {url}")
    driver.get(url)

    # Ждём полной загрузки страницы / Wait for the page to fully load
    log_step("Waiting for the page to load... / Ждём полной загрузки страницы...")
    time.sleep(5)

    # Получаем HTML-контент страницы / Retrieve the page HTML content
    log_step("Retrieving HTML content... / Получаем HTML-контент...")
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    text_content = soup.get_text().lower()  # Convert content to lowercase / Преобразуем текст в нижний регистр

    # Проверяем на признаки автоматизации / Check for automation flags
    log_step("Checking for automation flags... / Проверяем на признаки автоматизации...")
    automation_indicators = ["webdriver"]  # Automation detection flags / Флаги автоматизации
    detected_flags = [flag for flag in automation_indicators if flag in text_content]

    # Логируем результат / Log the result
    if detected_flags:
        log_step(f"Automation detected! Flags: {', '.join(detected_flags)} / Автоматизация распознана! Флаги: {', '.join(detected_flags)}")
    else:
        log_step("No automation detected. All clear. / Автоматизация не распознана. Все чисто.")

    # Сохраняем скриншот / Take a screenshot
    screenshot_path = "intoli_check_screenshot.png"
    log_step(f"Taking screenshot and saving as '{screenshot_path}' / Делаем скриншот и сохраняем как '{screenshot_path}'")
    driver.save_screenshot(screenshot_path)

except Exception as e:
    logging.error(f"An error occurred: {e} / Произошла ошибка: {e}")

finally:
    # Закрываем браузер / Close the browser
    if driver:
        log_step("Closing the browser. / Закрываем браузер.")
        driver.quit()