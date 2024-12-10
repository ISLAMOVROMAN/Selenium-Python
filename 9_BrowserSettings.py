from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Создаем объект настроек Chrome / Create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()

# Устанавливаем стратегию загрузки страницы "eager" (загрузка контента без ожидания загрузки всех ресурсов)
# Set the page load strategy to "eager" (loads content without waiting for all resources)
chrome_options.page_load_strategy = "normal"

# Устанавливаем размер окна браузера / Set the browser window size
chrome_options.add_argument("--window-size=1920,1080")

# Настраиваем сервис для использования ChromeDriver / Set up the service for ChromeDriver
service = Service(executable_path=ChromeDriverManager().install())

# Инициализируем веб-драйвер Chrome с заданными настройками / Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Замеряем время начала загрузки страницы / Record the start time of the page load
start_time = time.time()

# Открываем указанную веб-страницу / Open the specified web page
driver.get("https://whatismyipaddress.com")

# Замеряем время окончания загрузки страницы / Record the end time of the page load
end_time = time.time()

# Рассчитываем общее время загрузки страницы / Calculate the total page load time
result = end_time - start_time

# Выводим результат на экран / Print the result to the console
print(result)
