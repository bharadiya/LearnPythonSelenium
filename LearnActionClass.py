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
driver.get("https://demoqa.com/droppable")

wait = driver.implicitly_wait(10)

dragMe = driver.find_element(By.XPATH,"//div[@id='draggable']")
dropMe= driver.find_element(By.XPATH,"//div[@id='draggable']/following-sibling::div")

action = ActionChains(driver)

action.drag_and_drop(dragMe,dropMe).perform();

action.context_click(dropMe).perform()

