import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver,timeout=20)
time.sleep(10)

username = driver.find_element(By.XPATH,"//input[@name='username']")
# wait.until(EC.element_to_be_clickable(username))
password = driver.find_element(By.NAME,"password")

username.send_keys("Admin")
password.send_keys("admin123")
driver.find_element(By.XPATH,"//button[contains(text(),'')]").click()

time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Admin']").click();

time.sleep(5)
action = ActionChains(driver)
usernameCheckbox = driver.find_element(By.XPATH,"//div[text()='Username']/preceding-sibling::div//input")
action.click(usernameCheckbox).perform();

driver.save_screenshot('ss2.png')
screenshot = Image.open('ss.png')
screenshot.show()
