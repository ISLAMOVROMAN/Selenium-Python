import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера / Initialize the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Настройка явного ожидания / Set up explicit wait
wait = WebDriverWait(driver, 10, poll_frequency=1)

try:
    # Открытие страницы / Open the page
    driver.get("https://www.freeconferencecall.com/ru/il/login")
    print("Сайт успешно открыт. / The site has been successfully opened.")

    # Удаление всех существующих куков / Delete all existing cookies
    driver.delete_all_cookies()
    print("Все существующие куки удалены. / All existing cookies have been deleted.")

    # Загрузка куков из файла / Load cookies from file
    cookies_file_path = os.path.join(os.getcwd(), "cookies.pkl")
    if os.path.exists(cookies_file_path):
        with open(cookies_file_path, "rb") as cookies_file:
            cookies = pickle.load(cookies_file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        print(f"Куки загружены из файла: {cookies_file_path} / Cookies loaded from file: {cookies_file_path}")
    else:
        print(f"Файл с куками не найден: {cookies_file_path} / Cookies file not found: {cookies_file_path}")

    # Обновление страницы после добавления куков / Refresh page after adding cookies
    time.sleep(2)  # Пауза для корректной обработки / Pause for proper processing
    driver.refresh()
    print("Страница обновлена. / Page refreshed.")

except Exception as e:
    print(f"Произошла ошибка: {e} / An error occurred: {e}")

finally:
    # Закрытие браузера / Close the browser
    print("Закрытие браузера... / Closing the browser...")
    driver.quit()