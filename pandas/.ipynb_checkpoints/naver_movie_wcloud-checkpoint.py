import urllib
from bs4 import BeautifulSoup
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from soynlp.noun import NewsNounExtractor
from PIL import Image
import numpy as np


list_records=[]
for i in range(1,3):
    params=urllib.parse.urlencode({'page':i})
    url="https://movie.naver.com/movie/point/af/list.nhn?&%s" %params

    response=urllib.request.urlopen(url)
    bs = BeautifulSoup(response, 'html.parser')
    table=bs.find('table', class_='list_netizen')

    for i, r in enumerate(table.find_all('tr')):
        #print('i: ', i)
        #print('r: ', r)
        for j,c in enumerate(r.find_all('td')):
            #print('j: ', j)
            #print('c: ', c)
            if j==0:
                record={'번호':int(c.text.strip())}
            elif j==1:
                record.update({'영화':str(c.find('a').text.strip())})
                record.update({'140자 평':str(c.text.strip().replace('\n','').replace('\t',''))})
                record['140자 평']=record['140자 평'][len(record['영화']):-2]
            elif j==2:
                record.update({'글쓴이':c.find('a', class_='author').text.strip()})
                record.update({'날짜':str(c.text).split('****')[1]})
            
        try:
            list_records.append(record)
        except:
            pass


#print(list_records)

results=''
for record in list_records:
    results+=record['140자 평']

print(results)


stopwords_kr = []

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
        stopwords = stopwords_kr,
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

displayWordCloud(results)
