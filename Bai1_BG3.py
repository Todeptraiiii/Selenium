from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome()

# Mở trang demo có load dữ liệu chậm
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Nhấn nút "Start" để bắt đầu load dữ liệu
start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
start_button.click()

# Sử dụng Explicit Wait để chờ cho element có id "finish" xuất hiện và trở nên visible
wait = WebDriverWait(driver, 10)
finish_element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))

# In ra text của element (thường là "Hello World!")
print(finish_element.text)

# Đóng trình duyệt
driver.quit()
