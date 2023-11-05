import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://redbus.in")

time.sleep(5)

action= ActionChains(driver)
singapore=driver.find_element(By.XPATH,"//a[@id='singapore_site_footer']")

singapore.send_keys(Keys.CONTROL+Keys.ENTER)

# 2 windows / tabs

redBusTabs = driver.window_handles
print(redBusTabs)

for i in range(0,5):
    for j in range(0,len(redBusTabs)):
        driver.switch_to.window(redBusTabs[j])
        time.sleep(3)
