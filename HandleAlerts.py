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
driver.get("https://demoqa.com/alerts")

wait = driver.implicitly_wait(10)

confirmBtn = driver.find_element(By.ID,"promtButton")
action = ActionChains(driver)

action.click(confirmBtn).perform()

time.sleep(5)

al = Alert(driver)

time.sleep(5)
al.send_keys("Hi")
al.accept()
