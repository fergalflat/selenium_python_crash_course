from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)  # returns the title of the page
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
driver.close() # closes one tab at a time. driver.quit() closes the browser
