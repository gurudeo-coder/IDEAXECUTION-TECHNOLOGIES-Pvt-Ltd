import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

@pytest.fixture(autouse=True)
def start_automatic_fixture():
    print('start test with automatic fixture')

@pytest.fixture(scope='module')

def setup_teardown():
    driver.get('https://boom.tv/')
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign In').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'email').send_keys("gurudeo.padwe@gmail.com")
    time.sleep(2)
    driver.find_element(By.NAME, 'password').send_keys("123456")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="new_login_modal"]/div/div/div/form[1]/button').click()
    time.sleep(2)

    print("log In")
    yield
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign Out').click()
    print("logout")



@pytest.mark.usefixtures("setup_teardown")
def test1_apex():
    driver.get("https://boom.tv/")
    driver.implicitly_wait(10)

    driver.maximize_window()

    driver.find_element(By.PARTIAL_LINK_TEXT, 'Proving Grounds Ladies Night').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="event_header_tab"][1]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@class="header-overview"]//div[2]').click()
    time.sleep(5)
    driver.quit()







