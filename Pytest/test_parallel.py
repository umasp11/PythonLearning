#to run test parallely install this package >pip install pytest-xdist
#py.test test_parallel.py -n 4   it will execute in 4 browser

from selenium import webdriver
from  selenium.webdriver import ActionChains




def test_facebook():
    driver=webdriver.Chrome (executable_path="C:\\Users\\umasankar.panigrahy\Downloads\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get('http://www.facebook.com')
    assert driver.title=='Facebook – log in or sign up'
    driver.quit()

def test_google():
    driver=webdriver.Chrome (executable_path="C:\\Users\\umasankar.panigrahy\Downloads\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get('http://www.google.com')
    assert driver.title=='Google'
    driver.quit()

def test_gmail():
    driver=webdriver.Chrome (executable_path="C:\\Users\\umasankar.panigrahy\Downloads\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get('http://www.gmail.com')
    assert driver.title=='Gmail'
    driver.quit()

def test_youtube():
    driver=webdriver.Chrome (executable_path="C:\\Users\\umasankar.panigrahy\Downloads\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get('http://www.youtube.com')
    assert driver.title=='YouTube'
    driver.quit()