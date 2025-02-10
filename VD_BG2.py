from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  
driver.get("https://www.google.com")

# B1: Tìm ô tìm kiếm (locator: By.NAME, "q")
search_box = driver.find_element(By.NAME, "q")

# B2: Nhập từ khoá
search_box.send_keys("Selenium Python")

# B3: Nhấn Enter
search_box.send_keys(Keys.ENTER)

time.sleep(2)  # Chờ trang tải

# B4: In ra tiêu đề trang
print(driver.title)

driver.quit()
