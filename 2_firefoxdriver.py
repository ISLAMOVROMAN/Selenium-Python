from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# Initialize the WebDriver / Инициализация веб-драйвера
# Set up the Firefox WebDriver using GeckoDriverManager for automatic installation of the GeckoDriver.
# Настройка веб-драйвера Firefox с использованием GeckoDriverManager для автоматической установки GeckoDriver.
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
print("Firefox WebDriver initialized successfully.")  # WebDriver инициализирован успешно.

# Open a webpage / Открыть веб-страницу
# Use the `get` method to navigate to the specified URL.
# Используем метод `get`, чтобы перейти на указанный URL.
url = "https://www.google.com"
driver.get(url)
print(f"Website opened: {url}")  # Выводим URL, на который перешли.

# Interact with the webpage (if needed) / Взаимодействие с веб-страницей (если необходимо)
# At this step, you can add actions like finding elements, clicking buttons, or inputting text.
# На этом этапе можно добавить действия, такие как поиск элементов, нажатие кнопок или ввод текста.

# Close the browser / Закрытие браузера
# Use the `quit` method to terminate the browser session and release resources.
# Используем метод `quit`, чтобы завершить сессию браузера и освободить ресурсы.
driver.quit()
print("Browser session ended and resources released.")  # Сессия браузера завершена, ресурсы освобождены.