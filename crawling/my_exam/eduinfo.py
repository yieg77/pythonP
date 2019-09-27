import urllib.request
from bs4 import BeautifulSoup
import pymysql

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

conn = pymysql.connect(host='localhost',user='root',password='qwer1234',db='test',
charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor) #딕셔너리 형태로 데이터 출력
c=conn.cursor()

sql="""CREATE TABLE if not exists eduinfo(
    id integer,
    site text,
    title text,
    url text)"""

c.execute(sql)
conn.commit()
conn.close()
