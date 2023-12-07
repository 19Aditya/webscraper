from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url='https://quotes.toscrape.com/js/'
driver = webdriver.Chrome()
driver.get(url)
while True:
    rendered_html = driver.page_source
    soup = BeautifulSoup(rendered_html, 'html.parser')

    tag_list = driver.find_elements(By.CSS_SELECTOR, 'a.tag')#soup.select('a.tag')
    for tag in tag_list:
        print(tag.text)
    try:
        next_link = driver.find_element(By.CSS_SELECTOR, 'li.next a')
        next_link.click()
    except:
        break

