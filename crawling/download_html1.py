import urllib.request

url = 'https://www.naver.com'

mem = urllib.request.urlopen(url)
#print(mem.decode('euc-kr'))
print(mem.read().decode())#'utf-8'))

print(mem.info()) #encoing 정보 확인 가능.



