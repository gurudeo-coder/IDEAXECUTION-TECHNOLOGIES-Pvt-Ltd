import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get("https://boom.tv/")
driver.implicitly_wait(10)
time.sleep(2)
driver.maximize_window()

click_sign_In= driver.find_element(By.PARTIAL_LINK_TEXT,'Sign In')
time.sleep(2)
click_sign_Up= driver.find_element(By.PARTIAL_LINK_TEXT,'Sign Up')
time.sleep(2)

uesr_Name= driver.find_element(By.XPATH,'//*[@id="new_login_modal"]/div/div/div/form[2]/input[4]')
email_ID= driver.find_element(By.XPATH,'//*[@id="new_login_modal"]/div/div/div/form[2]/input[5]')
password= driver.find_element(By.XPATH,'//*[@id="admin_login_password"]')
confirm_password= driver.find_element(By.XPATH,'//*[@id="admin_login_password_confirmation"]')
click_Register= driver.find_element(By.XPATH,'//*[@id="admin_login_register_btn"]')

click_sign_In.click()
click_sign_Up.click()
uesr_Name.send_keys("gurudeo")
email_ID.send_keys("gurudeo.padwe@gmail.com")
password.send_keys("123456")
confirm_password.send_keys("123456")
click_Register.click()

assert driver.title == "BOOM.TV -LIVE"
print("Successful Regrister")
