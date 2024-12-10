from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Создаем объект настроек Chrome / Create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()

# Настройка папки для загрузки файлов / Setting up the download folder
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"  # Устанавливаем папку для загрузки / Set the folder for downloads
}
chrome_options.add_experimental_option("prefs", prefs)

# Настраиваем службу для ChromeDriver / Configure the service for ChromeDriver
service = Service(executable_path=ChromeDriverManager().install())

# Инициализируем WebDriver с настройками / Initialize WebDriver with options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открываем страницу для загрузки файлов / Open the file download page
driver.get("https://the-internet.herokuapp.com/download")
time.sleep(3)  # Ждем загрузки страницы / Wait for the page to load

# Находим и кликаем по четвертой ссылке на странице / Find and click on the fourth link on the page
driver.find_elements("xpath", "//a")[3].click()
time.sleep(3)  # Ждем завершения загрузки / Wait for the download to complete
