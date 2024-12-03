import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the driver / Инициализация драйвера
# Here we create an instance of the Chrome WebDriver using ChromeDriverManager for automatic driver installation.
# Здесь мы создаем экземпляр веб-драйвера Chrome, используя ChromeDriverManager для автоматической установки драйвера.
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Login data / Данные для входа
# Email and password values to be used for login.
# Значения email и пароля, которые будут использованы для входа на сайт.
email_value = "sladenkii@gmail.com"
password_value = "123457q"

try:
    # Open the website / Открытие сайта
    # Navigate to the specified website using the `get` method and log the current URL.
    # Переходим на указанный веб-сайт с помощью метода `get` и логируем текущий URL.
    driver.get("https://www.freeconferencecall.com")
    print("Website opened:", driver.current_url)

    # Retrieve and log the title of the page / Получение и логирование заголовка страницы
    # Extract and log the title of the current page to verify that the page has loaded correctly.
    # Извлекаем и логируем заголовок текущей страницы для подтверждения успешной загрузки.
    page_title = driver.title
    print(f"Page title: {page_title}")

    # Allow the page to fully load / Даем странице загрузиться полностью
    # Introduce a delay of 5 seconds to ensure all elements are fully loaded.
    # Задержка на 5 секунд для гарантии полной загрузки всех элементов.
    time.sleep(5)

    # Locate and enter email / Поиск и ввод email
    # Use an explicit wait to find the email input field. Raise an exception if not found within 10 seconds.
    # Используем явное ожидание для нахождения поля ввода email. Исключение поднимется, если элемент не найден в течение 10 секунд.
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Email')]"))
    )
    email_field.send_keys(email_value)
    print(f"Email entered: {email_value}")

    # Locate and enter password / Поиск и ввод пароля
    # Find the password input field in the same way as the email field and enter the password value.
    # Аналогично email, находим поле пароля и вводим значение.
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='user-password']"))
    )
    password_field.send_keys(password_value)
    print(f"Password entered: {password_value}")

    # Locate and click the "Create My Free Account" button / Поиск и клик по кнопке "Create My Free Account"
    # Search for the button using an explicit wait and click it once it becomes clickable.
    # Ищем кнопку с помощью явного ожидания и кликаем по ней, когда она становится доступной для взаимодействия.
    try:
        create_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create My Free Account')]"))
        )
        create_account_button.click()
        print("Click on 'Create My Free Account' button performed.")
    except Exception as e:
        # Handle the error if the button is not found / Обработка ошибки, если кнопка не найдена
        # If the button is not found, perform the following actions:
        # Если кнопка не найдена, выполняем следующие действия:
        print("Button 'Create My Free Account' not found.")

        # Save a screenshot of the page for debugging / Сохранение скриншота страницы для отладки
        driver.save_screenshot("create_account_error.png")
        print("Screenshot saved as 'create_account_error.png'.")

        # Print all buttons on the page for additional debugging / Вывод всех кнопок на странице для дополнительной отладки
        print("HTML content of buttons on the page:")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            print(button.get_attribute('outerHTML'))

        # Raise the exception to terminate the program / Поднимаем исключение, чтобы завершить выполнение программы с ошибкой
        raise e

except Exception as e:
    # General error handling block / Общий блок обработки ошибок
    # Log any general errors that occur during the script execution.
    # Логируем любые ошибки, возникшие во время выполнения скрипта.
    print("An error occurred:", str(e))
finally:
    # Close the browser / Закрытие браузера
    # Ensure the browser is closed after execution, regardless of the outcome.
    # Убеждаемся, что браузер закрыт после выполнения скрипта, независимо от результата.
    time.sleep(5)
    driver.quit()
    print("Browser closed.")