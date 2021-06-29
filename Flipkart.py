from selenium import webdriver

driver=webdriver.Chrome (r"C:\Users\umasankar.panigrahy\Downloads\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.flipkart.com/')

