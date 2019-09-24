import urllib.request
from bs4 import BeautifulSoup

rqst=urllib.request.Request("http://jfac.kr/contents/index.php?mid=070101")
response=urllib.request.urlopen(rqst)

#print(response.info())

soup = BeautifulSoup(response.read().decode('euc-kr'), 'html.parser')

print(soup)

print(soup.select("div > contents"))
