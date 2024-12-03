from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# Initialize the WebDriver / Инициализация веб-драйвера
# Create an instance of the Firefox WebDriver using GeckoDriverManager for automatic driver installation.
# Создаем экземпляр веб-драйвера Firefox, используя GeckoDriverManager для автоматической установки драйвера.
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Open a webpage / Открыть веб-страницу
# Navigate to the specified URL using the `get` method.
# Переходим по указанному URL с помощью метода `get`.
driver.get("https://www.google.com")
print("Website opened: https://www.google.com")

# Close the browser / Завершить работу браузера
# Ensure that the browser session is closed after execution to release resources.
# Убеждаемся, что сессия браузера завершена после выполнения, чтобы освободить ресурсы.
driver.quit()
print("Browser closed.")