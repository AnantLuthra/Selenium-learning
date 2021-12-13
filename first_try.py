from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver = webdriver.Chrome(service = s)
# driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
print("Going on sleep")

time.sleep(10)
print("After coming from sleep")

print("Given website link to open.")
driver.get("https://www.wix.com/")
print("Asked for title of the website.")
print(f"Title of given site is {driver.title}")
print("said for closing the one..")
driver.close()

