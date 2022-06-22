from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

def open_browser():
    driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')
    driver.implicitly_wait((10))
    return driver

def go_to_homepage(driver):
    driver.get('http://demostore.supersqa.com/')

def add_first_item_to_cart(driver):
    first_add_btn = driver.find_element_by_class_name('add_to_cart_button')
    first_add_btn.click()

def go_to_cart_page(driver):
    driver.get('http://demostore.supersqa.com/cart')

def apply_coupon(driver, coupon_code):
    coupon_field = driver.find_element_by_id('coupon_code')
    coupon_field.send_keys(coupon_code)
    apply_btn = driver.find_element_by_css_selector('#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button')
    apply_btn.click()

def verify_cart_has_item(driver):

    for i in range(5):
        try:
            driver.find_element_by_class_name('cart_item')
            return
        except NoSuchElementException:
            print("item not in cart")
            time.sleep(2)
            driver.refresh()

def get_error_message(driver):
    return driver.find_element_by_css_selector('#post-7 > div > div > div.woocommerce-notices-wrapper > ul > li').text


if __name__ == '__main__':
    open_browser()
    go_to_homepage(driver)
    add_first_item_to_cart(driver)
    go_to_cart_page(driver)
    apply_coupon(driver, 'fakeone')
    verify_cart_has_item(driver)
    get_error_message(driver)