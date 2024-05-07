# vim test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36")
options.add_argument("--accept-encoding=gzip, deflate, br, zstd")
options.add_argument("--disable-extensions")
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_argument("--disable-client-side-phishing-detection")
options.add_argument("--disable-popup-blocking")
options.add_argument("--force-dark-mode")
options.add_argument("--disable-composited-antialiasing")
options.add_argument("--disable-low-res-tiling")
options.add_argument("--log-level=3")
options.add_argument("--in-process-gpu")
options.add_argument("--incognito")
options.add_argument("--request-desktop-sites")
options.add_argument("--v8-cache-options=code")
options.add_argument("--enable-features=NetworkServiceInProcess")
options.add_argument("--start-maximized")
#options.add_argument("window-size=1920×1080")
options.add_argument("--disable-arc-cpu-restriction")
options.add_argument("--disable-cookie-encryption")
options.add_argument("--force-device-scale-factor=1")
driver = webdriver.Chrome(options=options)

driver.get("https://www.youtube.com/live/ByMgeelJNow?si=O6E_fa5XgYNXKTUn")
time.sleep(3)
#driver.save_screenshot("screenShot.png")
driver.find_element(By.CSS_SELECTOR, "button.ytp-large-play-button.ytp-button").click()
time.sleep(10)
#driver.save_screenshot("/home/runner/work/Test5/Test5/shhit/screenShot___.png")

print(driver.title)
time.sleep(3)
iii = 0
while True:
  iii+=1
  driver.save_screenshot(f"/home/runner/work/Test5/Test5/shhit/screenShot_{iii}_.png")
  time.sleep(60)
  print(f"Saved = {iii}")
  if iii == 99999999:
    break
  else:
    pass
driver.close()