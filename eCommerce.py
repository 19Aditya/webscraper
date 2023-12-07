from selenium import webdriver
import time

url='https://www.flipkart.com/search?q=nothing%202%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
pageSource = driver.page_source
import re
price_pattern = re.compile(r'<div class="_30jeq3 _1_WHN1">(.*?)</div>')
match = price_pattern.search(pageSource)
if match:
    price = match.group(1)
    print("Nothing phone 2 price sda  " + price)
else:
    print("Price element not found asdas .")
driver.quit()


   
