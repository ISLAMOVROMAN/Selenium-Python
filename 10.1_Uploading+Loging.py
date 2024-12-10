import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройка логирования / Logging setup
logging.basicConfig(
    level=logging.INFO,  # Устанавливаем уровень логирования / Set logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат сообщений / Message format
    handlers=[
        logging.FileHandler("selenium_log.log"),  # Лог в файл / Log to file
        logging.StreamHandler()  # Лог в консоль / Log to console
    ]
)

# Создаем логгер / Create logger
logger = logging.getLogger(__name__)

# Установка и запуск веб-драйвера / Setup and launch the web driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    logger.info("Открываем страницу / Opening the page")
    driver.get("https://www.freeconferencecall.com/login")
    
    # Ждем загрузки поля для ввода email / Wait for the email input field to load
    logger.info("Ждем загрузки поля для ввода email / Waiting for the email input field")
    login_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='login_email']"))
    )
    login_field.send_keys("selenium@ya.ru")  # Вводим email / Enter email
    logger.info("Email введен / Email entered")
    
    # Ждем появления поля для ввода пароля / Wait for the password input field to appear
    logger.info("Ждем появления поля для ввода пароля / Waiting for the password input field")
    password_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))
    )
    password_field.send_keys("123")  # Вводим пароль / Enter password
    logger.info("Пароль введен / Password entered")
    
    # Ждем появления кнопки и кликаем по ней / Wait for the submit button and click it
    logger.info("Ждем появления кнопки и кликаем по ней / Waiting for the submit button and clicking it")
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='loginformsubmit']"))
    )
    submit_button.click()  # Нажимаем кнопку "Отправить" / Click the "Submit" button
    logger.info("Кнопка нажата / Button clicked")

except Exception as e:
    # Обработка ошибок / Error handling
    logger.error(f"Произошла ошибка: {e}")  # Log the error message
finally:
    # Закрываем браузер / Close the browser
    logger.info("Закрываем браузер / Closing the browser")
    driver.quit()
