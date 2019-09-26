from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome('./selenium/chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(3)

id='yieg77'
pw='apdpfhd9675'


















"""
#이 코드는 자동입력방지로 연결됨
driver.find_element_by_name('id').send_keys(id)
driver.find_element_by_name('pw').send_keys(pw+'\n')
"""

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
time.sleep(1)

#driver.find_element_by_xpath('//*[@id="login_maintain"]/span[1]').click()
#time.sleep(1)



#네이버페이 페이지 크롤링
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')
#notices = soup.select('dl.my_npoint')


print("notices\n", notices)

point = soup.select_one('.my_npoint strong')
#print(point.string)
time.sleep(15)

driver.close()
