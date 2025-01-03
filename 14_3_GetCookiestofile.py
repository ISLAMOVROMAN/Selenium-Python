import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # Локаторы элементов / Element locators
    LOGIN_FIELD = (By.ID, "login_email")  # Локатор для поля email
    PASSWORD_FIELD = (By.ID, "password")  # Локатор для поля пароля
    SUBMIT_BUTTON = (By.ID, "loginformsubmit")  # Локатор для кнопки отправки

    # Ожидание элементов / Wait for elements
    wait.until(EC.presence_of_element_located(LOGIN_FIELD))
    wait.until(EC.presence_of_element_located(PASSWORD_FIELD))
    wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON))

    # Ввод данных для авторизации / Enter login credentials
    driver.find_element(*LOGIN_FIELD).send_keys("your_email@example.com")
    driver.find_element(*PASSWORD_FIELD).send_keys("your_password")
    driver.find_element(*SUBMIT_BUTTON).click()
    print("Авторизация выполнена. / Login performed.")

    # Сохранение куков в файл / Save cookies to file
    cookies_file_path = os.path.join(os.getcwd(), "cookies.pkl")
    with open(cookies_file_path, "wb") as cookies_file:
        pickle.dump(driver.get_cookies(), cookies_file)
    print(f"Куки сохранены в файл: {cookies_file_path} / Cookies saved to file: {cookies_file_path}")

except Exception as e:
    print(f"Произошла ошибка: {e} / An error occurred: {e}")

finally:
    # Закрытие браузера / Close the browser
    print("Закрытие браузера... / Closing the browser...")
    driver.quit()