import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://redbus.in")

source=driver.find_element(By.XPATH,"//input[@id='src']")
source.send_keys("Pune")

dest=driver.find_element(By.XPATH,"//label[text()='To']/preceding-sibling::input")
dest.send_keys("Mumbai")

time.sleep(5)
# dateClicker=driver.find_element(By.XPATH,"//span[text()='Date']")
# dateClicker.click()

searchBuses=driver.find_element(By.XPATH,"//button[text()='SEARCH BUSES']")
searchBuses.click()


# allanchorLinks = driver.find_elements(By.XPATH,"//a")
# print(allanchorLinks)
#
# act = ActionChains(driver)
# act.send_keys("HI").perform()
#
# driver.find_element(By.XPATH,"//input[@id='src']")

