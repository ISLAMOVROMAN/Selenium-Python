# Автор: [RomanIslamov]

# Описание: 
# Этот автотест создан для автоматического тестирования веб-формы на сайте demoqa.com. 
# Включает проверки текстовых полей, чекбоксов и кнопки отправки. 
# Используется Selenium WebDriver и язык программирования Python.

# Author: [Roman Islamov]
# Description:
# This automated test is designed to test the web form on the demoqa.com website.
# It includes validations for text fields, checkboxes, and the submit button.
# It uses Selenium WebDriver and Python programming language.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Конфигурация тестовых данных
# Test data configuration
TEST_DATA = {
    "first_name": ["A", "Alex", "A" * 255],
    "last_name": "Smith",
    "email": "test@example.com",
    "mobile": "1234567890",
    "hobbies": ["Sports", "Reading", "Music"]
}

# Настройка веб-драйвера
# Web driver setup
def setup_driver():
    # Устанавливаем драйвер Chrome и максимизируем окно
    # Set up Chrome driver and maximize the window
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

# Ожидание элемента
# Element wait function
def wait_for_element(driver, by, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))
    except Exception as e:
        print(f"Ошибка при ожидании элемента {locator}: {e}")
        print(f"Error while waiting for the element {locator}: {e}")
        return None

# Тестирование текстового поля
# Testing text fields
def test_text_field(driver, field_id, test_values):
    field = wait_for_element(driver, By.ID, field_id)
    if not field:
        return

    for value in test_values:
        try:
            field.clear()
            field.send_keys(value)
            print(f"Тест поля {field_id}: Ввод значения '{value}' (Passed)")
            print(f"Field {field_id} test: Entered value '{value}' (Passed)")
        except Exception as e:
            print(f"Ошибка при тестировании поля {field_id} с значением '{value}': {e}")
            print(f"Error testing field {field_id} with value '{value}': {e}")

# Тестирование чекбоксов
# Testing checkboxes
def test_checkboxes(driver, options):
    for option in options:
        try:
            checkbox = wait_for_element(driver, By.XPATH, f"//label[text()='{option}']")
            if checkbox:
                checkbox.click()
                print(f"Чекбокс '{option}' выбран (Passed)")
                print(f"Checkbox '{option}' selected (Passed)")
        except Exception as e:
            print(f"Ошибка при выборе чекбокса '{option}': {e}")
            print(f"Error selecting checkbox '{option}': {e}")

# Основной тест
# Main test function
def run_test():
    driver = setup_driver()
    try:
        # Открываем страницу
        # Open the page
        driver.get("https://demoqa.com/automation-practice-form")
        print("Страница открыта.")
        print("Page opened.")

        # Тестируем поле First Name
        # Testing the First Name field
        test_text_field(driver, "firstName", TEST_DATA["first_name"])

        # Тестируем поле Last Name
        # Testing the Last Name field
        test_text_field(driver, "lastName", [TEST_DATA["last_name"]])

        # Тестируем поле Email
        # Testing the Email field
        test_text_field(driver, "userEmail", [TEST_DATA["email"]])

        # Тестируем поле Mobile
        # Testing the Mobile field
        test_text_field(driver, "userNumber", [TEST_DATA["mobile"]])

        # Тестируем чекбоксы
        # Testing checkboxes
        test_checkboxes(driver, TEST_DATA["hobbies"])

        # Нажимаем кнопку Submit
        # Clicking the Submit button
        submit_button = wait_for_element(driver, By.ID, "submit")
        if submit_button:
            # Прокручиваем страницу к кнопке и кликаем по ней
            # Scroll to the button and click it
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            submit_button.click()
            print("Кнопка Submit нажата (Passed)")
            print("Submit button clicked (Passed)")

    except Exception as e:
        print(f"Общая ошибка: {e}")
        print(f"General error: {e}")

    finally:
        # Закрываем браузер
        # Closing the browser
        driver.quit()
        print("Браузер закрыт.")
        print("Browser closed.")

# Запуск теста
# Test execution
if __name__ == "__main__":
    run_test()
