import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера / Initializing the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы / Opening the page
    driver.get("https://www.freeconferencecall.com/login")
    print("Сайт успешно открыт. / The site has been successfully opened.")

    # Добавление новой куки / Adding a new cookie
    driver.add_cookie({"name": "Example", "value": "Kukushka"})
    print("Новая кука добавлена. / New cookie has been added.")

    # Получение конкретной куки / Getting a specific cookie
    example_cookie = driver.get_cookie("Example")
    print(f"Кука 'Example': {example_cookie} / Cookie 'Example': {example_cookie}")

except Exception as e:
    print(f"Произошла ошибка: {e} / An error occurred: {e}")

finally:
    # Закрытие браузера / Closing the browser
    print("Закрытие браузера... / Closing the browser...")
    driver.quit()