from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element_by_css_selector("#wizardMainRegionV2 > div > div > div > div > ul > li:nth-child(2) > a").click()
#driver.find_element(By.ID, "tab-flight-tab-hp")
time.sleep(5)
driver.find_element_by_id("location-field-leg1-origin-menu-trigger").send_keys("SFO")
time.sleep(2)
driver.find_element_by_id("location-field-leg1-destination-menu-trigger").send_keys("NYC")
