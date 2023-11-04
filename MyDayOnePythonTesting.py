import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# driver.minimize_window()
# driver.maximize_window()
driver.get("https://fb.com")

driver.back()
time.sleep(3)
driver.forward()

time.sleep(3)

title = driver.title
if title == "Facebook – log in or sign up":
    print("title is verified")
else:
    print("title is not verified")

email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
email.send_keys("Hi@gmail.com")
password = driver.find_element(By.NAME, "pass")
password.send_keys("kfhkdlfkdjkf")

driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
time.sleep(5)

selectDay = driver.find_element(By.XPATH, "//select[@aria-label='Day']")
tagSelect = Select(selectDay)
tagSelect.select_by_index(5)
tagSelect.select_by_value("21")

maleCheckBox=driver.find_element(By.XPATH,"//label[text()='Male']/following-sibling::input")
maleCheckBox.click()

driver.find_element(By.XPATH,"//label[text()='Male']/following-sibling::input").click()

driver.find_elements(By.XPATH,"//label[text()='Male']/following-sibling::input");
forgottonPassword = driver.find_element(By.XPATH, "//a[text()='Forgotten password?']")
forgottonPassword.click()

currentURL = driver.current_url
if currentURL == "https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0":
    print("url verified")
else:
    print("url not verified")

time.sleep(15)
