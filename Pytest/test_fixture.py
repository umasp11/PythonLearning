

from selenium import webdriver
from  selenium.webdriver import ActionChains

def setup_module(module):
    global driver
    driver= webdriver.Chrome (executable_path="C:\\Users\\umasankar.panigrahy\Downloads\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get('http://www.google.com')

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == 'Google'

def test_google_url():
    assert driver.current_url == 'https://www....m/?gws_rd=ssl'