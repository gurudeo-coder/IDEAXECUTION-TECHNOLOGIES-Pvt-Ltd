import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get("https://boom.tv/")
driver.implicitly_wait(10)
time.sleep(2)
driver.maximize_window()
time.sleep(2)

sign_In= driver.find_element(By.PARTIAL_LINK_TEXT,'Sign In')
email_ID= driver.find_element(By.NAME,'email')
password= driver.find_element(By.NAME,'password')
login= driver.find_element(By.XPATH,'//*[@id="new_login_modal"]/div/div/div/form[1]/button')

sign_In.click()
email_ID.send_keys("gurudeo.padwe@gmail.com")
password.send_keys("123456")
login.click()

assert driver.title == "BOOM.TV -LIVE"
print("successful login")
time.sleep(2)

logout= driver.find_element(By.PARTIAL_LINK_TEXT,'Sign Out' )
logout.click()
print("logout")

