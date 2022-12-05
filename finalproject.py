#coding=utf-8
import requests as re
from bs4 import BeautifulSoup as bs
import time 
import os
from collections import Counter
from matplotlib import pyplot as mt
from wordcloud import WordCloud
import jieba as jb

with open('test.txt','w',encoding='utf-8') as t:
        url = f'https://forum.gamer.com.tw/B.php?bsn=60076'
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
        res=re.get(url,headers=headers)
        soup=bs(res.text,'html.parser')
        articles=soup.find_all('p',class_='b-list__main__title')
        #print(type(articles))
        for link in articles:
            link=link.get("href")
            urls=f"https://forum.gamer.com.tw/{link}"
            resin=re.get(urls,headers=headers)
            soupin=bs(resin.text,'html.parser')
            innerarticles=soupin.find_all('div',class_="c-article__content")
            for innerart in innerarticles:
                t.write(innerart.text)
#jieba cut
jb.set_dictionary('dict.txt.big')
with open ('stops.txt','r',encoding='utf-8') as st:
    stops=st.read().split('\n')
    stops.append('\n')  
    stops.append('\n\n')
with open('test.txt','r',encoding='utf-8') as text:
    teststr=text.read()
terms = [t for t in jb.cut(teststr, cut_all=True) if t not in stops]
sorted(Counter(terms).items(), key=lambda x:x[1], reverse=True)  
wordcloud = WordCloud(font_path="simsun.ttf")
wordcloud.generate_from_frequencies(frequencies=Counter(terms))
fig=mt.figure(figsize=(15,15))
mt.imshow(wordcloud,interpolation="nearest")
mt.axis("off")
#mt.show()
fig.savefig('hw4.png')

