from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome()

# Mở trang web (ví dụ: Hacker News, vì trang này có cấu trúc tương tự)
driver.get("https://news.ycombinator.com/")

# Sử dụng explicit wait để chờ các phần tử có CSS selector "span.titleline a" xuất hiện (chờ tối đa 10 giây)
wait = WebDriverWait(driver, 10)
title_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.titleline a")))

# In ra text của từng tiêu đề bài viết
for link in title_links:
    print(link.text)

# Đóng trình duyệt
driver.quit()
