from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Инициализация драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

try:
    # Открываем веб-страницу
    logging.info("Открываем страницу")
    driver.get("https://demoqa.com/dynamic-properties")

    # Удаляем iframe рекламы, если он мешает
    try:
        logging.info("Проверяем наличие iframe рекламы")
        iframe = driver.find_element(By.XPATH, "//iframe[contains(@id,'google_ads_iframe')]")
        driver.execute_script("arguments[0].remove();", iframe)
        logging.info("Iframe рекламы успешно удален")
    except Exception as e:
        logging.info("Iframe рекламы не найден, продолжаем")

    # Явное ожидание, пока кнопка не станет кликабельной
    logging.info("Ожидаем, пока кнопка станет кликабельной")
    visible_after_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "visibleAfter"))
    )

    # Кликаем по кнопке
    logging.info("Кликаем по кнопке")
    visible_after_button.click()
    logging.info("Кнопка успешно нажата")

except Exception as e:
    logging.error(f"Произошла ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
    logging.info("Браузер закрыт")