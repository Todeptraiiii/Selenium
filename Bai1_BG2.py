from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo Chrome WebDriver (chú ý: cần cài đặt ChromeDriver tương thích với phiên bản Chrome của bạn)
driver = webdriver.Chrome()

# Mở trang đăng nhập
driver.get("https://the-internet.herokuapp.com/login")

# Tìm trường username theo ID "username"
username_field = driver.find_element(By.ID, "username")

# Tìm trường password theo ID "password"
password_field = driver.find_element(By.ID, "password")

# Nhập thông tin đăng nhập.
# Với trang này, thông tin hợp lệ là:
#    Username: tomsmith
#    Password: SuperSecretPassword!
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")

# Tìm nút Login bằng CSS_SELECTOR (có thể dùng By.TAG_NAME("button") cũng được)
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Click nút Login
login_button.click()

# Chờ trang chuyển đổi sau khi đăng nhập (có thể dùng explicit wait cho trường hợp thực tế)
time.sleep(2)

# Lấy thông báo hiển thị trên trang (thông thường nằm trong element có ID "flash")
flash_element = driver.find_element(By.ID, "flash")
flash_text = flash_element.text

# Kiểm tra thông báo và in ra kết quả
if "You logged into a secure area!" in flash_text:
    print("Login successful")
else:
    print("Login failed")

# Đóng trình duyệt
driver.quit()
