from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

driver.get('https://www.python.org/')
driver.implicitly_wait(10)
cur_title = driver.title
expected_title  = 'Welcome to Python.org'

if cur_title != expected_title:
    raise Exception("Wrong title")

search_field_id = 'id-search-field'
search_field_elm =  driver.find_element_by_id(search_field_id)
search_field_elm.send_keys('testing')

go_btn_id = 'submit'
go_btn_elm = driver.find_element_by_id(go_btn_id)
go_btn_elm.click()

first_result_xpath = '//*[@id="content"]/div/section/form/ul/li[1]'
first_result_elm = driver.find_element_by_xpath(first_result_xpath)

#import pdb; pdb.set_trace()

if first_result_elm.is_displayed():
    print("Pass")
else:
    raise Exception("error")
