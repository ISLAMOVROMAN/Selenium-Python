import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка логирования / Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler("test_log.log"),  # Логирование в файл / Logging to a file
        logging.StreamHandler()  # Логирование в консоль / Logging to console
    ]
)

# Настройка веб-драйвера / Setting up WebDriver
logging.info("Инициализация веб-драйвера / Initializing WebDriver")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Настройка явного ожидания / Setting up explicit wait
wait = WebDriverWait(driver, 15, poll_frequency=1)

try:
    # Открываем страницу / Opening the webpage
    logging.info("Открываем веб-страницу / Opening the webpage")
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    # Определяем элементы / Defining elements
    ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")  # Кнопка "Enable" / Enable button
    TEXT_FIELD = ("xpath", "//input[@type='text']")  # Текстовое поле / Text input field

    # Нажимаем на кнопку "Enable" / Clicking the "Enable" button
    logging.info("Ожидание кликабельности кнопки 'Enable' / Waiting for 'Enable' button to be clickable")
    wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
    logging.info("Кнопка 'Enable' нажата / 'Enable' button clicked")
    time.sleep(2)  # Задержка для демонстрации / Delay for demonstration

    # Ввод текста в поле / Entering text into the field
    logging.info("Ожидание кликабельности текстового поля / Waiting for the text field to be clickable")
    wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")
    logging.info("Текст 'Hello' введен в поле / Text 'Hello' entered into the field")
    time.sleep(2)  # Задержка для демонстрации / Delay for demonstration

    # Проверяем, что текст появился в поле / Verifying that the text is present in the field
    logging.info("Проверка, что текст 'Hello' появился в поле / Verifying that 'Hello' is present in the field")
    wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello"))
    logging.info("Текст 'Hello' успешно найден в поле / 'Hello' text successfully found in the field")

    print("ВСЁ OK / Test passed successfully")
    logging.info("Тест успешно завершен / Test completed successfully")

except Exception as e:
    logging.error(f"Произошла ошибка: {e} / An error occurred: {e}")

finally:
    # Закрываем драйвер / Closing the driver
    logging.info("Закрытие веб-драйвера / Closing WebDriver")
    driver.quit()
