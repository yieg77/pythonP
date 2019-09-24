import urllib.parse, urllib.request

param = {'sm':'top_hty','fbm':'1', 'ie':'utf8', 'query':'urllib'}

query=input("검색어를 입력하세요 : ")
param['query']=query
print(param)

data1 = urllib.parse.urlencode(param)#, quote_via=urllib.parse.quote)
print(data1)

#data2 = urllib.parse.urlencode(param)
#print(data2)

pages=urllib.request.urlopen("https://search.naver.com/search.naver?"+data1)
print(pages.read().decode())
