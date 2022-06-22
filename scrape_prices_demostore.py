from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')
driver.implicitly_wait(5)
url = 'http://demostore.supersqa.com/'
driver.get(url)

all_products = driver.find_elements(By.CLASS_NAME, 'product')
print(f"Number of products: {len(all_products)}")

all_products_and_price = []
for product in all_products:
    price_elm = product.find_element(By.CSS_SELECTOR, 'span.amount')
    price = price_elm.text

    name_elm = product.find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
    name = name_elm.text
    print(price)
    print(name)
    all_products_and_price.append({'name': name, 'price': price})

print(len(all_products_and_price))
print(all_products_and_price)