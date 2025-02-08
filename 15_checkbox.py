from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

CHECKBOX_1 = "//input[@type='checkbox'][1]"

driver.get("http://the-internet.herokuapp.com/checkboxes")
time.sleep(3)

print(driver.find_element("xpath", CHECKBOX_1).is_selected())
driver.find_element("xpath", CHECKBOX_1).click()
print(driver.find_element("xpath", CHECKBOX_1).is_selected())

time.sleep(3)
driver.quit()