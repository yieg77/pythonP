import urllib.request, os
from bs4 import BeautifulSoup

rqst=urllib.request.Request("http://www.cgv.co.kr/movies/")
response=urllib.request.urlopen(rqst)

#print(response.info())

soup = BeautifulSoup(response.read().decode(), 'html.parser')

print(soup)

print(soup.select("box-image"))




"""
dirname=os.path.dirname(__file__)
savename=dirname+'/test.png'

urllib.request.urlretrieve(url, savename)

"""
