# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os, sys, json, pymysql, datetime
import urllib.request
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from soynlp.noun import NewsNounExtractor
from PIL import Image

client_id = "lJYukXCk5Do4WahIXYrm"
client_secret = "h0i136cKQB"










conn = pymysql.connect(host='localhost',user='root',password='qwer1234',db='test',
charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor) #딕셔너리 형태로 데이터 출력
c=conn.cursor()

sql="""CREATE TABLE if not exists naver_news(
    title text,
    originallink text,
    link text,
    description text,
    pubDate datetime)"""
c.execute(sql)

sql="""ALTER TABLE `test`.`naver_news` CONVERT TO CHARSET utf8mb4"""
c.execute(sql)



encText = urllib.parse.quote("제주")
#print(encText)

results=''
for i in range (1, 30, 10):
    url = "https://openapi.naver.com/v1/search/news.json?display=10&start="+str(i)+"&sort=sim&query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    #print(url)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        results=response_body.decode('utf-8')

        a=json.loads(results)
        items=a['items']
        #print('items', type(items), items)
        contents=''#item_list=[]
        for i in range(len(items)):
            d=BeautifulSoup(items[i]['description'], 'html.parser')
            contents+=d.get_text()
    else:
        print("Error Code:" + rescode)




print(contents)



def displayWordCloud(data=None, backgroundcolor='white', width=800, height=600):
    #이미지 형태대로 wordcloud 출력
    img = Image.open('./pandas/apple.png')
    img_array=np.array(img)

    #soynlp로 명사만 빼내기
    noun_extractor = NewsNounExtractor()
    nouns=noun_extractor.train_extract([results])
    print(type(nouns))

    wordcloud = WordCloud(
        font_path = '/Library/Fonts/HMKMAMI.TTF',
        #font_path = 'C:/Windows/Fonts/HMKMAMI.TTF',
        #stopwords = stopwords_kr,
        background_color=backgroundcolor,
        mask=img_array,
        width=width,
        height=height).generate(' '.join(nouns))

    print(wordcloud.words_)
    plt.figure(figsize=(15,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
   
    wordcloud.to_file('./pandas/result.png')

#displayWordCloud(response_body)


'''
        a=json.loads(results)
        items=a['items']
        #print('items', type(items), items)
        item_list=[]
        for i in range(len(items)):
            t=BeautifulSoup(items[i]['title'], 'html.parser')
            #print(t.prettify())
            #print(t.get_text())
            d=BeautifulSoup(items[i]['description'], 'html.parser')
            #datetime.time
            z=datetime.datetime.strptime('Fri, 27 Sep 2019 05:44:00',"%a, %d %b %Y %H:%M:%S")
            #print(type(z), z)

            each_data=[t.get_text(), items[i]['originallink'], items[i]['link'], d.get_text(), items[i]['pubDate']]
            item_list.append(each_data)

        print('item_list', type(item_list), item_list)
        sql="INSERT INTO naver_news VALUES (%s,%s,%s,%s,%s)"
        c.executemany(sql, item_list)
    else:
        print("Error Code:" + rescode)
'''
#conn.commit()
conn.close()

