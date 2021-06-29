#PyTest with Selenium and Integration with Jenkins and Allure Reporting

import pytest
from selenium import webdriver
import allure

@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Chrome (r"C:\Users\umasankar.panigrahy\Downloads\chromedriver_win32\chromedriver.exe")
    driver.maximize_window()
    yield
    driver.quit()

@allure.description('test login with vaid credential')
@allure.severity(severity_level='critical')
def test_validLogin(test_setup):
    driver.get("https://orangehrm-demo-6x.orangehrmlive.com")
    driver.find_element_by_id('txtUsername').clear()
    driver.find_element_by_id('txtUsername').send_keys('admin')
    driver.find_element_by_id('txtPassword').clear()
    driver.find_element_by_id('txtPassword').send_keys('admin123')

    driver.find_element_by_id('btnLogin').click()
    assert  'dashboard' in driver.current_url

@allure.description('test login with invaid credential')
@allure.severity(severity_level='normal')
def test_invalidLogin(test_setup):
    driver.get("https://orangehrm-demo-6x.orangehrmlive.com")
    driver.find_element_by_id('txtUsername').clear()
    driver.find_element_by_id('txtUsername').send_keys('admin')
    driver.find_element_by_id('txtPassword').clear()
    driver.find_element_by_id('txtPassword').send_keys('admin')
    driver.find_element_by_id('btnLogin').click()

    try:
        assert 'dashboard' in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(),name='invalid credential',attachment_type=allure.attachment_type.PNG)