from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Настройка веб-драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открыть страницу (пример)
driver.get("https://www.yandex.ru")

# Завершить работу
driver.quit()