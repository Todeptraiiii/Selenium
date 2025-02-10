from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome()

# Mở trang demo kéo-thả
driver.get("https://jqueryui.com/droppable/")

# Trang demo chứa nội dung kéo-thả nằm trong iframe nên cần chuyển sang iframe đó
iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
driver.switch_to.frame(iframe)

# Tìm phần tử cần kéo (draggable) và vùng thả (droppable)
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

# Tạo đối tượng ActionChains và thực hiện kéo-thả
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# Chờ một chút để kết quả hiển thị (trong demo sau khi thả, text của droppable thường thay đổi thành "Dropped!")
time.sleep(2)

# Kiểm tra kết quả hiển thị (lấy text của vùng droppable)
result_text = droppable.text
print("Kết quả hiển thị sau khi kéo-thả:", result_text)

# Quay lại default content (nếu cần thực hiện thao tác ngoài iframe)
driver.switch_to.default_content()

# Đóng trình duyệt
driver.quit()
