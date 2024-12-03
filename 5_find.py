from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка веб-драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Переход на указанную страницу
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(3)  # Ждём загрузки страницы

    # Найти иконку Wikipedia по имени класса
    wikipedia_icon = driver.find_element(By.CLASS_NAME, "wikipedia-icon")
    print("Иконка Wikipedia найдена:", wikipedia_icon)

    # Найти поле ввода Wikipedia по id
    wikipedia_input = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
    print("Поле ввода Wikipedia найдено:", wikipedia_input)

    # Найти кнопку поиска Wikipedia по классу
    wikipedia_search_button = driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
    print("Кнопка поиска Wikipedia найдена:", wikipedia_search_button)

    # Найти любой другой элемент на странице по тегу
    any_element = driver.find_element(By.TAG_NAME, "h2")  # Например, первый заголовок на странице
    print("Элемент найден по тегу:", any_element.text)

finally:
    # Закрыть браузер
    time.sleep(5)
    driver.quit()