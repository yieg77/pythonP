from bs4 import BeautifulSoup
from selenium import webdriver
import time
#import requests #urllib와 비슷

driver=webdriver.Chrome('./selenium/chromedriver')
driver.get("https://www.istarbucks.co.kr/index.do")
time.sleep(10)

menu=driver.find_element_by_class_name('ally')
menu.click()
time.sleep(10)
"""
loca=driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(10)

sido=driver.find_element_by_class_name('sido_arae_box')
li=sido.find_elements_by_tag_name('li')
li[5].click()
time.sleep(10)

sido = driver.find_element_by_class_name('gugun_arae_box')
li=sido.find_elements_by_tag_name('li')
li[6].click()
time.sleep(10)

source=driver.page_source

bs=BeautifulSoup(source, 'lxml')
entire=bs.find('ul', class_='quickSearchResultBoxSidoGugun')
lis=entire.find_all('li')

for li in lis:
    print(li.find('p').text)
"""
