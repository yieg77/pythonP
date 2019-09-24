import urllib.parse

parse = urllib.parse.urlparse('192.168.147.128/bWAPP/portal.php?id=bee&pw=bug#example', scheme='http')
print(parse)

parse = urllib.parse.urlparse('192.168.147.128/bWAPP/portal.php?id=bee&pw=bug#example', scheme='http', allow_fragments=False) 
print(parse)

print(parse.path)

url=urllib.parse.urlunparse(parse) 
print(url)