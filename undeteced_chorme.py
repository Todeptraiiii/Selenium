from seleniumbase import Driver
import time

driver = Driver(uc=True)
driver.get("https://chat.zalo.me/")
time.sleep(5)
driver.quit()