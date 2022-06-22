from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

driver.get("http://newtours.demoaut.com/")
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in")
print(driver.title)
time.sleep(5)
driver.back()
time.sleep(5)
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)