from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

driver.get('https://www.python.org/')

cur_title = driver.title
expected_title  = 'Welcome to Python.org'

if cur_title != expected_title:
    raise Exception("Wrong title")

pypi_header_link_locator = '#top > nav > ul > li.pypi-meta > a'
pypi_header_link_elm = driver.find_element_by_css_selector(pypi_header_link_locator)
pypi_header_link_elm.click()

cur_url = driver.current_url

expected_url = 'https://pypi.org/'
assert cur_url == expected_url, f"clicked on pypi but the url opened was: {cur_url}"
print("PASS")