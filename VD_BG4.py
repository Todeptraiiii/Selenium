from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

# Step 1: switch to iframe
iframe = driver.find_element(By.ID, "mce_0_ifr")  # iframe ID
driver.switch_to.frame(iframe)

# Step 2: nhập text vào editor
editor = driver.find_element(By.ID, "tinymce")
editor.clear()  # xóa text mặc định
editor.send_keys("Hello from Selenium ActionChains & iframe!")

time.sleep(1)

# Step 3: quay lại trang chính, click link
driver.switch_to.default_content()
driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()

# Có thể link này mở tab mới; ta quay lại tab cũ hoặc
# driver.back() tùy ý — Ở đây ví dụ ta back:
driver.back()

# Bây giờ quay sang trang drag_and_drop
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

time.sleep(1)

# Step 4: Thực hiện kéo-thả 2 khối
column_a = driver.find_element(By.ID, "column-a")
column_b = driver.find_element(By.ID, "column-b")

actions = ActionChains(driver)
actions.drag_and_drop(column_a, column_b).perform()

time.sleep(2)
driver.quit()
