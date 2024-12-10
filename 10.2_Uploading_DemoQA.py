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
        logging.FileHandler("upload_test_log.log"),  # Лог в файл / Log to file
        logging.StreamHandler()  # Лог в консоль / Log to console
    ]
)

# Создаем логгер / Create logger
logger = logging.getLogger(__name__)

# Путь к файлу, который будет загружен / Path to the file to be uploaded
file_path = "/Users/admin/PycharmProjects/Selenium/Downloads/Examplefile.txt"

# Установка и запуск веб-драйвера / Setup and launch the web driver
service = Service(ChromeDriverManager().install())  # Устанавливаем ChromeDriver / Install ChromeDriver
driver = webdriver.Chrome(service=service)  # Инициализируем драйвер / Initialize driver

try:
    logger.info("Открываем страницу / Opening the page")
    driver.get("https://demoqa.com/upload-download")  # Открываем целевую страницу / Open the target page
    
    # Ждем загрузки страницы и находим элемент для загрузки файла / Wait for the page to load and locate the upload element
    logger.info("Ждем появления поля для загрузки файла / Waiting for the upload input field")
    upload_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='uploadFile']"))  # Ищем элемент загрузки по XPATH / Locate upload element using XPATH
    )
    
    # Загрузка файла / Upload the file
    logger.info(f"Загружаем файл: {file_path} / Uploading file: {file_path}")
    upload_field.send_keys(file_path)  # Загружаем файл с помощью send_keys / Upload file using send_keys
    logger.info("Файл успешно загружен / File uploaded successfully")
    
    # Проверяем успешную загрузку (проверяем наличие текста с путем файла) / Validate successful upload (check the text with file path)
    uploaded_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "uploadedFilePath"))  # Ищем текст с подтверждением загрузки / Locate confirmation text
    )
    logger.info(f"Загруженный файл: {uploaded_text.text} / Uploaded file: {uploaded_text.text}")

except Exception as e:
    # Обработка ошибок / Error handling
    logger.error(f"Произошла ошибка: {e}")  # Логируем сообщение об ошибке / Log the error message
finally:
    # Закрываем браузер / Close the browser
    logger.info("Закрываем браузер / Closing the browser")
    driver.quit()  # Завершаем работу драйвера / Quit the driver
