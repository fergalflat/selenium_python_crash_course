
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

driver.get('http://demostore.supersqa.com')
print(driver.title)
