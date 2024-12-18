import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize ChromeDriver via Service / Инициализация ChromeDriver через Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Set up explicit wait / Настройка явного ожидания
wait = WebDriverWait(driver, 10, poll_frequency=1)

try:
    # Open the page / Открытие страницы
    driver.get("https://demoqa.com/alerts")
    print("The site has been successfully opened. / Сайт успешно открыт.")

    # Locator for the button that triggers the alert / Локатор кнопки для вызова алерта
    ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")

    # Wait for the button to be clickable and click it / Ожидание кликабельности кнопки и клик по ней
    print("Waiting for the alert button to be clickable... / Ожидание кликабельности кнопки с алертом...")
    wait.until(EC.element_to_be_clickable(ALERT_BUTTON)).click()
    print("The alert button has been clicked. / Кнопка с алертом нажата.")

    # Wait for the alert to appear / Ожидание появления алерта
    print("Waiting for the alert to appear... / Ожидание появления алерта...")
    alert = wait.until(EC.alert_is_present())

    # Work with the alert / Работа с алертом
    print(f"Alert text: {alert.text} / Текст алерта: {alert.text}")
    time.sleep(2)  # Pause for visual check / Пауза для визуальной проверки
    alert.accept()
    print("The alert has been accepted. / Алерт успешно принят.")

except Exception as e:
    # Print error message if any issue occurs / Вывод сообщения об ошибке при возникновении проблемы
    print(f"An error occurred: {e} / Произошла ошибка: {e}")

finally:
    # Close the browser / Завершение работы драйвера
    print("Closing the browser... / Закрытие браузера...")
    driver.quit()