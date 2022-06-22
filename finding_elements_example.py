from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pdb

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

driver.get('http://demostore.supersqa.com')
#By ID
cart = driver.find_element_by_id("site-header-cart")
print(cart)
print(type(cart))

cart_txt = cart.text
print(cart_txt)

#By ID
search_field = driver.find_element_by_id("woocommerce-product-search-field-0")
search_field.send_keys("hoodie")
#search_field.send_keys(Keys.ENTER)

#By CSS Selector
#my_acct = driver.find_element_by_css_selector("#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9")
#my_acct.click()

pdb.set_trace()

#driver.quit()
#driver.close()