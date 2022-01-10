# python_crawler_program
#coding=utf-8
import requests as re
from bs4 import BeautifulSoup as bs
import time as t 
import os
url = 'https://www.ptt.cc/bbs/index.html'
header={'referer': 'https://www.ptt.cc/bbs/index.html','user-agent': 'Mozilla/5.0'}
cookies={'over18': '1'}
res=re.get(url,headers=header,cookies=cookies)
soup=bs(res.text,'html.parser')
#tys=soup.find_all('div',class_='board-class')
board=soup.find_all('a',class_='board')
#titles=soup.find_all('div',class_='board-title')
'''for contents,title,ty in zip(board,titles,tys):
    print(ty.text)
    print(title.text) 
    print('https://www.ptt.cc/'+contents.get('href'))
    print('\n')'''
#爬取第一層網頁名稱連結
for i,item in enumerate(board):
        print(i,item.find('div',class_='board-title').text)
        content='連結:https://www.ptt.cc{}'.format(item.get('href'))
        print(content)
        content=content.strip('連結:')
        res1=re.get(content,headers=header,cookies=cookies)
        sp=bs(res1.text,'html.parser')
        inner_titles=sp.find_all('div',class_='title')
#爬取第一層連結內網址的各個文章標題
        for i,inti in enumerate(inner_titles):
            if inti.find('a'):
                print('\t',i+1,inti.a.text)
            else :
                print('\t',i+1,'(本文已被刪除) [disgusting]')

