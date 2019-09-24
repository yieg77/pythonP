import urllib.request

"""
response=urllib.request.urlopen("http://naver.com")

print(response)

print(response.geturl())
print(response.getcode())

print(response.info())
print(response.read().decode())
"""

rqst=urllib.request.Request("http://naver.com")
response=urllib.request.urlopen(rqst)

print(rqst.full_url)
print(rqst.type)
print(rqst.host)
print(rqst.origin_req_host)
print(response.read().decode())
print(rqst.get_method())
rqst.method="POST"
print(rqst.get_method())

