from bs4 import BeautifulSoup
from selenium import webdriver
import time
#import requests #urllib와 비슷

driver=webdriver.Chrome('./selenium/chromedriver.exe')
#driver.get("https://www.istarbucks.co.kr/store/store_map.do")
#driver.get("https://www.istarbucks.co.kr/store/store_map.do")
driver.get("https://www.google.com/maps")
time.sleep(4)

inputElement = driver.find_element_by_id('searchboxinput')
inputElement.send_keys("카카오\n")
#inputElement2 = driver.find_element_by_id('searchbox-searchbutton')
#inputElement2.click()
time.sleep(4)

#addr=driver.find_element_by_class_name('section-result-location')
#print(addr.text)

pages=driver.page_source
bs=BeautifulSoup(pages, "html.parser")
#print(bs)

title=bs.select("h3.section-result-title span")
results=bs.select("span.section-result-location")

type(results)

for i in range(len(results)):
    print(title[i].string, " : ", results[i].string)


"""
menu=driver.find_element_by_id('quickSearchText')
menu.click()
time.sleep(4)

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
