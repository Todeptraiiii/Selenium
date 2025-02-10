from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome()

# Mở trang upload file
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(1)  # Chờ trang tải xong

# Tìm input file theo id "file-upload"
upload_input = driver.find_element(By.ID, "file-upload")

# Lưu ý: Bạn cần thay đổi đường dẫn dưới đây thành đường dẫn tuyệt đối tới file trên máy của bạn.
# Ví dụ, trên Windows: "C:\\Users\\YourUsername\\Documents\\example.txt"
# Trên Mac/Linux: "/Users/YourUsername/Documents/example.txt"
file_path = "C:\\Users\\Van To\\Downloads\\clk156.pcap"
upload_input.send_keys(file_path)

# Tìm nút Upload theo id "file-submit" và click
upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()

# Chờ kết quả tải lên hiển thị
time.sleep(2)

# Lấy kết quả (thường là một element <h3> hiển thị thông báo upload thành công)
result_text = driver.find_element(By.TAG_NAME, "h3").text
print("Kết quả sau khi upload:", result_text)

# Đóng trình duyệt
driver.quit()
