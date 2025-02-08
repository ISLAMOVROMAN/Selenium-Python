import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Установка веб-драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Локаторы радиокнопок
YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")  # Для статуса
YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']")  # Для взаимодействия
IMPRESSIVE_RADIO_BUTTON = ("xpath", "//input[@id='impressiveRadio']")  # Для статуса
IMPRESSIVE_RADIO_LABEL = ("xpath", "//label[@for='impressiveRadio']")  # Для взаимодействия
NO_RADIO_BUTTON = ("xpath", "//input[@id='noRadio']")

try:
    # Открытие страницы с радиокнопками
    driver.get("https://demoqa.com/radio-button")
    time.sleep(2)

    # Проверка доступности кнопки "No"
    assert driver.find_element(*NO_RADIO_BUTTON).is_enabled() is False, "Кнопка 'No' доступна"
    print("Кнопка 'No' недоступна (disabled)")

    # Клик на кнопку "Yes"
    driver.find_element(*YES_RADIO_LABEL).click()
    time.sleep(1)

    # Проверка, что кнопка "Yes" выбрана
    assert driver.find_element(*YES_RADIO_BUTTON).is_selected() is True, "Радио-кнопка 'Yes' не выбрана"
    print("Радио-кнопка 'Yes' успешно выбрана")

    # Клик на кнопку "Impressive"
    driver.find_element(*IMPRESSIVE_RADIO_LABEL).click()
    time.sleep(1)

    # Проверка, что кнопка "Impressive" выбрана
    assert driver.find_element(*IMPRESSIVE_RADIO_BUTTON).is_selected() is True, "Радио-кнопка 'Impressive' не выбрана"
    print("Радио-кнопка 'Impressive' успешно выбрана")

finally:
    # Закрытие браузера
    time.sleep(2)
    driver.quit()