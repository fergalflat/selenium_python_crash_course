from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

driver.get("https://demo.guru99.com/test/newtours/")

driver.implicitly_wait(10)
print(driver.title)
assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("submit").click()

