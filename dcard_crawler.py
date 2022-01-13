#coding=utf-8
import requests as re
from bs4 import BeautifulSoup as bs
import time as t 
import os
    
url='https://www.dcard.tw/f'
header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
res=re.get(url,headers=header)
soup=bs(res.text,'html.parser')
arts=soup.find_all('article',class_='tgn9uw-0 dRhFWg')
for i,art in enumerate(arts):
    if art.find():
        h2=art.find('h2',class_='tgn9uw-2 bqeEAL')
        if h2:
            #標題
            print(i+1,art.a.text)
            link=('https://www.dcard.tw/'+art.a.get('href'))
            #內文
            res=re.get(link,headers=header)
            t.sleep(2)
            soup=bs(res.text,'html.parser')
            cons=soup.find_all('article',class_='sc-1eorkjw-0 btVgIM')
            for inner in cons:
                print('\t',inner.text)
        else :print('沒東西')
    else : print('文章不存在')

