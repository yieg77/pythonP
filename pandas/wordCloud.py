import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from soynlp.noun import NewsNounExtractor
from PIL import Image
#%matplotlib inline  # 주피터에서 작업 시 세팅

f=open('./pandas/[박경리]_토지1.txt','r')
story = f.read()
#print(story)
f.close()

stopwords_kr = ['있었다','것이다','하지만','그리고','그러나','그런데','저는','제가','그럼','이런','저런','합니다','많은','많이','정말','너무','[',']','것으로','했습니다','했다','있다']

def displayWordCloud(data=None, backgroundcolor='white', width=800, height=600):
    #이미지 형태대로 wordcloud 출력
    img = Image.open('./pandas/apple.png')
    img_array=np.array(img)

    #soynlp로 명사만 빼내기
    noun_extractor = NewsNounExtractor()
    nouns=noun_extractor.train_extract([story])
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

displayWordCloud(story)


