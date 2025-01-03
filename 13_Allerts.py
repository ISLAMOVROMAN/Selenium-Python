import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера / Initializing the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Настройка явного ожидания / Setting up explicit wait
wait = WebDriverWait(driver, 10, poll_frequency=1)

try:
    # Открытие страницы / Opening the page
    driver.get("https://demoqa.com/alerts")
    print("Сайт успешно открыт. / The site has been successfully opened.")

    # Обработка первого алерта / Handling the first alert
    ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")
    wait.until(EC.element_to_be_clickable(ALERT_BUTTON)).click()  # Клик по кнопке алерта / Clicking the alert button
    alert = wait.until(EC.alert_is_present())  # Ожидание появления алерта / Waiting for the alert to appear
    print(f"Текст первого алерта: {alert.text} / First alert text: {alert.text}")
    time.sleep(2)  # Задержка для визуального эффекта / Pause for visual check
    alert.accept()  # Принятие алерта / Accepting the alert
    print("Первый алерт успешно принят. / The first alert has been accepted.")

    # Обработка второго алерта (с таймером) / Handling the second alert (with a timer)
    TIMER_ALERT_BUTTON = (By.XPATH, "//button[@id='timerAlertButton']")

    # Скрытие перекрывающего iframe / Hiding the overlapping iframe
    driver.execute_script(
        "document.getElementById('google_ads_iframe_/21849154601,22343295815/Ad.Plus-Anchor_0').style.display='none';"
    )

    # Клик по кнопке / Clicking the button
    timer_button = wait.until(EC.presence_of_element_located(TIMER_ALERT_BUTTON))
    driver.execute_script("arguments[0].scrollIntoView(true);", timer_button)  # Прокрутка к кнопке / Scrolling to the button
    wait.until(EC.element_to_be_clickable(TIMER_ALERT_BUTTON)).click()
    print("Ожидание появления второго алерта... / Waiting for the second alert to appear...")
    alert = wait.until(EC.alert_is_present())  # Ожидание алерта / Waiting for the alert
    print(f"Текст второго алерта: {alert.text} / Second alert text: {alert.text}")
    alert.accept()  # Принятие алерта / Accepting the alert
    print("Второй алерт успешно принят. / The second alert has been accepted.")

    # Обработка третьего алерта (подтверждение) / Handling the third alert (confirmation)
    CONFIRM_BUTTON = (By.XPATH, "//button[@id='confirmButton']")
    wait.until(EC.element_to_be_clickable(CONFIRM_BUTTON)).click()  # Клик по кнопке / Clicking the button
    print("Ожидание появления третьего алерта... / Waiting for the third alert to appear...")
    alert = wait.until(EC.alert_is_present())  # Ожидание алерта / Waiting for the alert
    print(f"Текст третьего алерта: {alert.text} / Third alert text: {alert.text}")
    alert.dismiss()  # Отмена алерта / Dismissing the alert
    print("Третий алерт успешно отменён. / The third alert has been dismissed.")

    # Обработка четвёртого алерта (prompt) / Handling the fourth alert (prompt)
    PROMPT_BUTTON = (By.XPATH, "//button[@id='promtButton']")
    wait.until(EC.element_to_be_clickable(PROMPT_BUTTON)).click()  # Клик по кнопке / Clicking the button
    print("Ожидание появления четвёртого алерта... / Waiting for the fourth alert to appear...")
    alert = wait.until(EC.alert_is_present())  # Ожидание алерта / Waiting for the alert
    print(f"Текст четвёртого алерта: {alert.text} / Fourth alert text: {alert.text}")
    alert.send_keys("Тестовое сообщение")  # Ввод текста в prompt / Entering text in the prompt
    alert.accept()  # Принятие алерта / Accepting the alert
    print("Четвёртый алерт успешно принят с вводом текста. / The fourth alert has been accepted with input.")

except Exception as e:
    print(f"Произошла ошибка: {e} / An error occurred: {e}")

finally:
    # Закрытие браузера / Closing the browser
    print("Закрытие браузера... / Closing the browser...")
    driver.quit()
