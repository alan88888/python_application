#coding=utf-8
import requests as re
from bs4 import BeautifulSoup as bs
import time 
import os
from requests.models import Response

num=1
with open('沒有編號和水桶和公告版本.txt','w',encoding='utf-8') as t:
    while num<=100:
        url = f'https://www.ptt.cc/bbs/MobileComm/index{num}.html'
        header={'referer': 'https://www.ptt.cc/bbs/index.html','user-agent': 'Mozilla/5.0'}
        cookies={'over18': '1'}
        res=re.get(url,headers=header,cookies=cookies)
        soup=bs(res.text,'html.parser')
        titles=soup.find_all('div',class_='title')
        t.write(f'第{num}頁\n')
        keyword='水桶'
        keyword1='公告'
        for i,title in enumerate(titles):
            if (keyword and keyword1) not in title.a.text :    
                #t.write(f'\t{i+1}')
                t.write(f'\t{title.a.text}')
                t.write('\n')
            else:
                continue
        num=num+1
        #time.sleep(1)

