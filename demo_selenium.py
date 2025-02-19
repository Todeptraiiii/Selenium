from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# B1: Khởi tạo driver (Chrome)
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

# B2: Mở một trang web
driver.get("https://www.google.com")

# B3: Tìm ô tìm kiếm Google theo 'name' và nhập nội dung
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")

time.sleep(2)  # chờ 2 giây để xem thao tác

# B4: Tự động nhấn Enter hoặc click nút
search_box.submit()

time.sleep(3)  # chờ 3 giây để xem kết quả

# B5: Đóng trình duyệt
driver.quit()


