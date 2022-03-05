from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
​
# Set chrome options for working with headless mode (no screen)
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
#chrome_options.add_argument("no-sandbox")
#chrome_options.add_argument("disable-dev-shm-usage")
​
# Update webdriver instance of chrome-driver with adding chrome options
driver = webdriver.Chrome("C:\chromedriver.exe", options=chrome_options)
driver.implicitly_wait(100)
# driver = webdriver.Chrome("/Users/home/Desktop/chromedriver")
# Connect to the application
# APP_IP = os.environ['MASTER_PUBLIC_IP']
url = "http://3.235.63.90:8080/"
# url = "http://localhost:8080"
print(url)
driver.get(url)
sleep(5)
owners_link = driver.find_element_by_link_text("OWNERS")
owners_link.click()
sleep(4)
all_link = driver.find_element_by_link_text("ALL")
all_link.click()
sleep(4)
​
# Verify that table loaded
sleep(1)
verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
​
print("Table loaded")
​
driver.quit()