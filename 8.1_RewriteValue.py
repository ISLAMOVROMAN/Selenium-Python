from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Конфигурация тестовых данных
TEST_DATA = {
    "first_name": ["A", "Alex", "A" * 255],
    "last_name": "Smith",
    "email": "test@example.com",
    "mobile": "1234567890",
    "hobbies": ["Sports", "Reading", "Music"]
}

# Настройка веб-драйвера
def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

# Ожидание элемента
def wait_for_element(driver, by, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))
    except Exception as e:
        print(f"Ошибка при ожидании элемента {locator}: {e}")
        return None

# Тестирование текстового поля
def test_text_field(driver, field_id, test_values):
    field = wait_for_element(driver, By.ID, field_id)
    if not field:
        return

    for value in test_values:
        try:
            field.clear()
            field.send_keys(value)
            print(f"Тест поля {field_id}: Ввод значения '{value}' (Passed)")
        except Exception as e:
            print(f"Ошибка при тестировании поля {field_id} с значением '{value}': {e}")

# Тестирование чекбоксов
def test_checkboxes(driver, options):
    for option in options:
        try:
            checkbox = wait_for_element(driver, By.XPATH, f"//label[text()='{option}']")
            if checkbox:
                driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
                checkbox.click()
                print(f"Чекбокс '{option}' выбран (Passed)")
        except Exception as e:
            print(f"Ошибка при выборе чекбокса '{option}': {e}")

# Тестирование обязательных полей
def test_required_fields(driver):
    try:
        submit_button = wait_for_element(driver, By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        if alert:
            print("Тест обязательных полей: Алёрт появился (Passed)")
    except Exception as e:
        print(f"Ошибка при тестировании обязательных полей: {e}")

# Основной тест
def run_test():
    driver = setup_driver()
    try:
        # Открываем страницу
        driver.get("https://demoqa.com/automation-practice-form")
        print("Страница открыта.")

        # Тестируем поле First Name
        test_text_field(driver, "firstName", TEST_DATA["first_name"])

        # Тестируем поле Last Name
        test_text_field(driver, "lastName", [TEST_DATA["last_name"]])

        # Тестируем поле Email
        test_text_field(driver, "userEmail", [TEST_DATA["email"]])

        # Тестируем поле Mobile
        test_text_field(driver, "userNumber", [TEST_DATA["mobile"]])

        # Тестируем чекбоксы
        test_checkboxes(driver, TEST_DATA["hobbies"])

        # Проверяем обязательные поля
        test_required_fields(driver)

        # Нажимаем кнопку Submit
        submit_button = wait_for_element(driver, By.ID, "submit")
        if submit_button:
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            submit_button.click()
            print("Кнопка Submit нажата (Passed)")

    except Exception as e:
        print(f"Общая ошибка: {e}")

    finally:
        driver.quit()
        print("Браузер закрыт.")

# Запуск теста
if __name__ == "__main__":
    run_test()
