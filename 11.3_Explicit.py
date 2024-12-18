from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Logging setup / Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize ChromeDriver / Инициализация драйвера Chrome
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Set an implicit wait / Устанавливаем неявное ожидание
driver.implicitly_wait(10)

try:
    # Open the web page / Открываем веб-страницу
    logging.info("Opening the page... / Открываем страницу...")
    driver.get("https://demoqa.com/dynamic-properties")

    # Remove iframe ads if they are present / Удаляем iframe рекламы, если он присутствует
    try:
        logging.info("Checking for iframe ads... / Проверяем наличие iframe рекламы...")
        iframe = driver.find_element(By.XPATH, "//iframe[contains(@id,'google_ads_iframe')]")
        driver.execute_script("arguments[0].remove();", iframe)
        logging.info("Iframe ads removed successfully. / Iframe рекламы успешно удален.")
    except Exception as e:
        logging.info("No iframe ads found, continuing... / Iframe рекламы не найден, продолжаем...")

    # Explicit wait for the button to become clickable / Явное ожидание, пока кнопка не станет кликабельной
    logging.info("Waiting for the button to become clickable... / Ожидаем, пока кнопка станет кликабельной...")
    visible_after_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "visibleAfter"))
    )

    # Click the button / Кликаем по кнопке
    logging.info("Clicking the button... / Кликаем по кнопке...")
    visible_after_button.click()
    logging.info("The button was clicked successfully. / Кнопка успешно нажата.")

except Exception as e:
    # Log any errors that occur / Логируем возникшие ошибки
    logging.error(f"An error occurred: {e} / Произошла ошибка: {e}")

finally:
    # Close the browser / Закрываем браузер
    driver.quit()
    logging.info("The browser has been closed. / Браузер закрыт.")
