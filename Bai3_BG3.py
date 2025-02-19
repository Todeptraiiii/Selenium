from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome()

# Mở trang demo chứa các alert
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# ---------------------------
# 1. Xử lý JS Alert (alert đơn giản)
# ---------------------------
# Tìm nút "Click for JS Alert" và click
alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
alert_button.click()

# Chuyển sang alert và chấp nhận alert
alert = driver.switch_to.alert
alert.accept()

# Lấy kết quả hiển thị trên trang (element có id="result")
result_text = driver.find_element(By.ID, "result").text
print("Kết quả sau khi accept JS Alert:", result_text)

time.sleep(1)  # Chờ một chút giữa các thao tác

# ---------------------------
# 2. Xử lý JS Confirm (alert confirm)
# ---------------------------

# a) Accept confirm alert
confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button.click()

confirm_alert = driver.switch_to.alert
confirm_alert.accept()  # Nhấn OK
result_text = driver.find_element(By.ID, "result").text
print("Kết quả sau khi accept JS Confirm:", result_text)

time.sleep(1)

# b) Dismiss confirm alert
confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button.click()

confirm_alert = driver.switch_to.alert
confirm_alert.dismiss()  # Nhấn Cancel
result_text = driver.find_element(By.ID, "result").text
print("Kết quả sau khi dismiss JS Confirm:", result_text)

time.sleep(1)

# ---------------------------
# 3. Xử lý JS Prompt (alert prompt)
# ---------------------------
prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
prompt_button.click()

prompt_alert = driver.switch_to.alert
# Gửi một chuỗi vào prompt
prompt_alert.send_keys("Hello Selenium")
prompt_alert.accept()  # Nhấn OK

result_text = driver.find_element(By.ID, "result").text
print("Kết quả sau khi nhập text vào JS Prompt:", result_text)

# Đóng trình duyệt
driver.quit()
