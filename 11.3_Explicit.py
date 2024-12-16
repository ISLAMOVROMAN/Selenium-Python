import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")

try:
    wait = WebDriverWait(driver, 30)

    logging.info("Начало выполнения скрипта")

    # 1. Дождитесь исчезновения текста
    logging.info("Ожидание исчезновения текста с ID 'deletesuccess'")
    wait.until(EC.invisibility_of_element_located((By.ID, "deletesuccess")))
    logging.info("Текст с ID 'deletesuccess' исчез")

    # 2. Дождитесь появления текста
    logging.info("Ожидание появления текста с ID 'delayedText'")
    text_element = wait.until(EC.visibility_of_element_located((By.ID, "delayedText")))
    logging.info(f"Текст появился: {text_element.text}")

    # 3. Дождитесь состояния enabled кнопки
    logging.info("Ожидание состояния enabled для кнопки с ID 'timerButton'")
    button_enable = wait.until(EC.element_to_be_clickable((By.ID, "timerButton")))
    logging.info("Кнопка 'timerButton' стала enabled")

    # 4. Клик по кнопке "Try it", чтобы отключить "My Button"
    logging.info("Поиск кнопки 'Try it'")
    try_button = driver.find_element(By.XPATH, "//button[text()='Try it']")
    logging.info("Кнопка 'Try it' найдена, выполняем клик")
    try_button.click()
    logging.info("Кнопка 'Try it' нажата")

    # Дождитесь состояния disabled кнопки "My Button"
    logging.info("Ожидание состояния disabled для кнопки 'My Button'")
    wait.until(EC.element_attribute_to_include((By.ID, "myBtn"), "disabled"))
    logging.info("Кнопка 'My Button' стала disabled")

    logging.info("Скрипт успешно завершен")

except Exception as e:
    logging.error(f"Произошла ошибка: {e}")
finally:
    logging.info("Закрытие браузера")
    driver.quit()