import urllib.request, os

url='http://post.phinf.naver.net/MjAxNzA0MTBfMzMg/MDAxNDkxODExNDA1OTUz.522JGGQcI7je8ZheiKBIEEKpYnAgV3gNxpZEaRJ1fdcg.F7Li-r3qncjmtCCqx8dYPGuc_s3yzGbW9ebEcR12_EEg.PNG/I3RMLB-FgBpiEyCq2BYgXAm03Z18.jpg'

dirname=os.path.dirname(__file__)
savename=dirname+'/test.png'

urllib.request.urlretrieve(url, savename)

"""
mem=urllib.request.urlopen(url).read()
with open(savename, mode='wb') as f:
    f.write(mem)
    print('저장 완료')
"""

