from selenium import webdriver  # Импорт библиотеки Selenium WebDriver / Import Selenium WebDriver library
from selenium.webdriver.common.by import By  # Импорт селекторов для поиска элементов / Import selectors for finding elements
from selenium.webdriver.chrome.service import Service  # Импорт класса Service для работы с драйвером Chrome / Import Service class for Chrome driver
from selenium.webdriver.support.ui import WebDriverWait  # Импорт WebDriverWait для ожидания элементов / Import WebDriverWait for waiting for elements
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания / Import expected conditions
from webdriver_manager.chrome import ChromeDriverManager  # Менеджер для автоматической установки ChromeDriver / Manager for automatic ChromeDriver installation
import time  # Импорт библиотеки для работы с временем / Import library for time management

# Конфигурация тестовых данных / Test data configuration
TEST_DATA = {
    "first_name": ["A", "Alex", "A" * 255],  # Тестовые значения для поля "Имя" / Test values for the "First Name" field
    "last_name": "Smith",  # Значение для поля "Фамилия" / Value for the "Last Name" field
    "email": "test@example.com",  # Значение для поля "Email" / Value for the "Email" field
    "mobile": "1234567890",  # Значение для поля "Мобильный телефон" / Value for the "Mobile Number" field
    "hobbies": ["Sports", "Reading", "Music"]  # Список хобби для тестирования чекбоксов / List of hobbies for checkbox testing
}

# Настройка веб-драйвера / WebDriver setup
def setup_driver():
    # Устанавливаем и запускаем ChromeDriver / Install and launch ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()  # Максимизируем окно браузера / Maximize the browser window
    return driver

# Ожидание элемента / Waiting for an element
def wait_for_element(driver, by, locator, timeout=10):
    try:
        # Ждём, пока элемент не станет видимым / Wait until the element becomes visible
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))
    except Exception as e:
        # Логируем ошибку, если элемент не найден / Log the error if the element is not found
        print(f"Ошибка при ожидании элемента {locator}: {e}")
        return None

# Тестирование текстового поля / Testing text fields
def test_text_field(driver, field_id, test_values):
    field = wait_for_element(driver, By.ID, field_id)  # Поиск поля по ID / Find the field by ID
    if not field:
        return

    for value in test_values:
        try:
            field.clear()  # Очищаем поле перед вводом нового значения / Clear the field before entering a new value
            field.send_keys(value)  # Вводим значение в поле / Enter the value into the field
            print(f"Тест поля {field_id}: Ввод значения '{value}' (Passed)")
        except Exception as e:
            print(f"Ошибка при тестировании поля {field_id} с значением '{value}': {e}")

# Тестирование чекбок
