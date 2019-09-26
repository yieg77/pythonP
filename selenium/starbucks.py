from bs4 import BeautifulSoup
from selenium import webdriver
import time
#import requests #urllib와 비슷

driver=webdriver.Chrome('./selenium/chromedriver.exe')
driver.get("https://www.istarbucks.co.kr/store/store_map.do")
driver.get("https://www.istarbucks.co.kr/store/store_map.do")
time.sleep(3)

#inputElement = driver.find_element_by_id('searchboxinput')
#inputElement.send_keys("카카오\n")
#inputElement2 = driver.find_element_by_id('searchbox-searchbutton')
#inputElement2.click()
time.sleep(3)

#addr=driver.find_element_by_class_name('section-result-location')
#print(addr.text)

loca=driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(3)

"""
loca=driver.find_element_by_class_name('set_sido_cd_btn')
loca.click()
time.sleep(4)
"""
sido=driver.find_element_by_class_name('sido_arae_box')
li=sido.find_elements_by_tag_name('li')
li[15].click()
time.sleep(2)

gugun = driver.find_element_by_class_name('gugun_arae_box')
li=gugun.find_elements_by_tag_name('li')
li[2].click()
time.sleep(2)

"""
source=driver.page_source
bs=BeautifulSoup(source, 'lxml')
entire=bs.find('ul', class_='quickSearchResultBoxSidoGugun')
lis=entire.find_all('li')

#print(lis)

for li in lis:
    print(li.find('strong').text, end=" : ")
    print(li.find('p').text)
"""

pages=driver.page_source
bs=BeautifulSoup(pages, "html.parser")
#print(bs)


#title=bs.select("h3.section-result-title span")
titles=bs.select("ul.quickSearchResultBoxSidoGugun strong")
addrs=bs.select("ul.quickSearchResultBoxSidoGugun p")
#tels=bs.select("li.quickResultLstCon p.result_details")

#print(titles[0].text)
#print(addrs[0].text)

for i in range(len(titles)):
    print(titles[i].text, " : ", addrs[i].text)

