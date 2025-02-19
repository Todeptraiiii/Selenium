from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome()

# Mở trang A
driver.get("https://the-internet.herokuapp.com/windows")
print("Tiêu đề của tab A:", driver.title)

# Tìm và click vào link mở tab mới (tab B)
link = driver.find_element(By.LINK_TEXT, "Click Here")
link.click()

# Chờ một chút để tab mới mở ra
time.sleep(1)

# Lấy danh sách các window handles (các tab, cửa sổ hiện có)
handles = driver.window_handles
print("Danh sách các window handles:", handles)

# Giả sử tab A là handles[0] và tab B là handles[1]
# Chuyển sang tab B
driver.switch_to.window(handles[1])
print("Tiêu đề của tab B:", driver.title)

# Đóng tab B
driver.close()

# Chuyển lại về tab A (ở handles[0])
driver.switch_to.window(handles[0])
print("Tiêu đề của tab A sau khi đóng tab B:", driver.title)

# Kết thúc, đóng trình duyệt
driver.quit()
