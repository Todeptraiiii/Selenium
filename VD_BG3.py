from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.implicitly_wait(5)  # Dùng Implicit Wait

# 1) Click "Click for JS Alert"
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(1)  # tạm dừng ngắn để xem alert

try:
    alert = driver.switch_to.alert
    print("Alert 1 text:", alert.text)
    alert.accept()
except NoAlertPresentException:
    print("No alert present #1")

# 2) Click "Click for JS Confirm"
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(1)

try:
    alert = driver.switch_to.alert
    print("Alert 2 text:", alert.text)
    alert.dismiss()  # bấm Cancel
except NoAlertPresentException:
    print("No alert present #2")

# 3) Click "Click for JS Prompt"
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(1)

try:
    alert = driver.switch_to.alert
    print("Alert 3 text:", alert.text)
    alert.send_keys("Hello")
    alert.accept()
except NoAlertPresentException:
    print("No alert present #3")

# In kết quả
result = driver.find_element(By.ID, "result").text
print("Result text:", result)

driver.quit()
