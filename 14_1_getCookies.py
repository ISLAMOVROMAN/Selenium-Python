import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера / Initializing the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Настройка явного ожидания / Setting up explicit wait
wait = WebDriverWait(driver, 10, poll_frequency=1)

try:
    # Открытие страницы / Opening the page
    driver.get("https://www.freeconferencecall.com/login")
    print("Сайт успешно открыт. / The site has been successfully opened.")

    # Получение конкретного кука / Getting a specific cookie
    country_cookie = driver.get_cookie("country_code")
    print(f"Кука country_code: {country_cookie} / Cookie country_code: {country_cookie}")

    # Получение всех кук / Getting all cookies
    all_cookies = driver.get_cookies()
    print(f"Все куки: {all_cookies} / All cookies: {all_cookies}")

    # Пример добавления нового кука / Example of adding a new cookie
    new_cookie = {
        "name": "test_cookie",
        "value": "test_value",
        "domain": "freeconferencecall.com"
    }
    driver.add_cookie(new_cookie)
    print("Новая кука добавлена. / New cookie added.")

    # Проверка добавленных кук / Checking added cookies
    print("Обновлённые куки: ", driver.get_cookies())

except Exception as e:
    print(f"Произошла ошибка: {e} / An error occurred: {e}")

finally:
    # Закрытие браузера / Closing the browser
    print("Закрытие браузера... / Closing the browser...")
    driver.quit()