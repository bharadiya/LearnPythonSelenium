import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://fb.com")

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
selectTag = Select(selectDay)
selectTag.select_by_index(5)

driver.find_element(By.XPATH,"//label[text()='Male']/following-sibling::input").click()
# forgottonPassword = driver.find_element(By.XPATH, "//a[text()='Forgotten password?']")
# forgottonPassword.click()
#
# currentURL = driver.current_url
# if currentURL == "https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0":
#     print("url verified")
# else:
#     print("url not verified")

time.sleep(15)
