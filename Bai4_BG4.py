import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Xác định thư mục tải file (Download folder)
download_dir = r"C:\Users\Van To\Downloads"  # Thay đổi đường dẫn này theo ý bạn

# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# 2. Thiết lập ChromeOptions để tự động download
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,      # Đặt thư mục download mặc định
    "download.prompt_for_download": False,           # Tắt hộp thoại hỏi xác nhận download
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True                     # Tắt bảo vệ an toàn có thể gây cản trở download
}
chrome_options.add_experimental_option("prefs", prefs)

# Khởi tạo ChromeDriver với các tùy chọn trên
driver = webdriver.Chrome(options=chrome_options)

# 3. Mở trang download
driver.get("https://the-internet.herokuapp.com/download")
time.sleep(2)  # Chờ trang tải xong

# 4. Click vào link download một file
# Lấy phần tử link đầu tiên trong danh sách (các link thường nằm trong <div class="example">)
file_link = driver.find_element(By.CSS_SELECTOR, "div.example a")
file_name = file_link.text  # Tên file sẽ được lấy từ text của link
print("Đang download file:", file_name)
file_link.click()

# 5. Chờ vài giây để file tải xong (có thể điều chỉnh thời gian nếu file lớn)
time.sleep(5)

# Đóng trình duyệt
driver.quit()

# 6. Kiểm tra file đã được download chưa
downloaded_file_path = os.path.join(download_dir, file_name)
if os.path.exists(downloaded_file_path):
    print("Download thành công! File được lưu tại:", downloaded_file_path)
else:
    print("Download không thành công, không tìm thấy file tại:", downloaded_file_path)
