import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[contains(text(),'')]").click()
time.sleep(5)
navAdmin = driver.find_element(By.XPATH,"//span[text()='Admin']")
navAdmin.click();
time.sleep(5)
usernameCheckbox =driver.find_element(By.XPATH,"(//input[@type='checkbox'])[3]")
usernameCheckbox.click();
