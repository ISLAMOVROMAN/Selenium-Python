from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Initialize the WebDriver / Инициализация веб-драйвера
# Set up the Chrome WebDriver using ChromeDriverManager for automatic installation of the ChromeDriver.
# Настройка веб-драйвера Chrome с использованием ChromeDriverManager для автоматической установки ChromeDriver.
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
print("Chrome WebDriver initialized successfully.")  # WebDriver для Chrome успешно инициализирован.

# Open a webpage / Открыть веб-страницу
# Use the `get` method to navigate to the specified URL.
# Используем метод `get`, чтобы перейти на указанный URL.
url_to_open = "https://www.wikipedia.org/"
driver.get(url_to_open)
print(f"Website opened: {url_to_open}")  # Выводим URL, на который перешли.

# Retrieve and log the current URL and title of the page / Получение и логирование текущего URL и заголовка страницы
# The `current_url` property fetches the URL of the currently loaded webpage.
# Свойство `current_url` возвращает URL загруженной веб-страницы.
current_url = driver.current_url
print(f"Current URL: {current_url}")  # Вывод текущего URL.

# The `title` property fetches the title of the currently loaded webpage.
# Свойство `title` возвращает заголовок загруженной веб-страницы.
page_title = driver.title
print(f"Current page title: {page_title}")  # Вывод текущего заголовка страницы.

# Pause the script for a few seconds / Пауза в работе скрипта на несколько секунд
# Use `