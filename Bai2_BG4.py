from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome()

# Mở trang demo có iframe TinyMCE
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(1)  # Chờ trang tải

# --- Bước 1: Chuyển vào iframe chứa trình soạn thảo ---
# Ở trang này, iframe có id là "mce_0_ifr"
iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

# --- Bước 2: Tìm vùng soạn thảo và thêm văn bản ---
# Vùng soạn thảo có id là "tinymce"
editor = driver.find_element(By.ID, "tinymce")
editor.clear()  # Xóa nội dung cũ

# Thêm văn bản mới vào editor
editor.send_keys("Hello, world! This text should be bolded.")

# --- Bước 3: (Tùy chọn) Định dạng văn bản ---
# Để định dạng (ví dụ: bôi đậm) văn bản, ta cần chọn toàn bộ văn bản.
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Chuyển ra khỏi iframe để tương tác với thanh công cụ TinyMCE
driver.switch_to.default_content()
time.sleep(1)

# Tìm và click nút Bold trên thanh công cụ
# Thông thường, nút Bold có thuộc tính title="Bold"
bold_button = driver.find_element(By.XPATH, "//button[@title='Bold']")
bold_button.click()

# Để kiểm tra kết quả định dạng, chuyển lại vào iframe và lấy HTML của vùng soạn thảo
driver.switch_to.frame(iframe)
formatted_html = editor.get_attribute("innerHTML")
print("Nội dung HTML sau khi định dạng:", formatted_html)

# --- Bước 4: Quay về document chính ---
driver.switch_to.default_content()

# In ra tiêu đề của trang để kiểm tra đã thoát iframe thành công
print("Tiêu đề trang:", driver.title)

# Dừng lại một chút trước khi đóng trình duyệt
time.sleep(2)
driver.quit()
