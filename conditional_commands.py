from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

driver.get("https://demo.guru99.com/test/newtours/")

element_usr = driver.find_element_by_name("userName")
element_pwd = driver.find_element_by_name("password")
print(element_usr.is_displayed())
print(element_usr.is_enabled())
print(element_pwd.is_displayed())
print(element_pwd.is_enabled())

element_usr.send_keys("mercury")
element_pwd.send_keys("mercury")

driver.find_element_by_name("submit").click()

driver.find_element_by_css_selector("body > div:nth-child(5) > table > tbody > tr > td:nth-child(1) > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > a")

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print(roundtrip_radio.is_selected())

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print(onetrip_radio.is_selected())
