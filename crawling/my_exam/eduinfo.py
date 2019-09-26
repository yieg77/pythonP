import urllib.request
from bs4 import BeautifulSoup

rqst=urllib.request.Request("http://jfac.kr/contents/index.php?mid=070101&page=1")
response=urllib.request.urlopen(rqst)

#print(response.info())

soup = BeautifulSoup(response.read().decode('euc-kr'), 'html.parser')

#print(soup)

#print(soup.select("div.contents"))

#print(soup.select("#layer_board_list tr td a title"))

results=soup.select("td.list_subject > a")
for result in results:
    print(result.attrs['title'], result.attrs['href'])




