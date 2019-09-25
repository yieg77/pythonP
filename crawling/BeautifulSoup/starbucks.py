import urllib.request
from bs4 import BeautifulSoup

url="https://www.istarbucks.co.kr/store/store_map.do?disp=quick"

pages=urllib.request.urlopen(url, 'html.parser')

