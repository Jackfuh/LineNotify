# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:51:53 2019

@author: Jack
"""

from bs4 import BeautifulSoup
import requests
url = 'https://www.tsmc.com/tsmcdotcom/PRListingNewsAction.do?language=E'
#url = 'https://www.tsmc.com.tw/tsmcdotcom/PRListingNewsAction.do?language=C'

def LatestNews(url):
    html = requests.get(url)
    html.encoding="utf-8"
    
    sp = BeautifulSoup(html.text, "html.parser")
    links = sp.find_all('a',{"title":"Latest News"})
    return links[0], links[1]
    #同時讀取 <a> 和 <屬性 title = Latest News>
    
    #for link in links:
    #    href=link.get("href") #讀取href內容
    #    if href!= None and href.startswith("http://"):
    #        print(href)
    #for n in range (0, len(links)):
    #    print(links[n].text,end="  ")

#-------------------------------------------------------------
def lineNotifyMessage(token, msg):
      headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
	
      payload = {'message': msg}
      r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
      return r.status_code
	

#-------------------------------------------------------------

from datetime import datetime 
from threading import Timer 
#打印時間函數
def printTime (inc) :
    
    #message = 'ttt' # 修改為你要傳送的訊息內容
    token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # 修改為你的權杖內容
    lineNotifyMessage(token, LatestNews(url))
    lineNotifyMessage(token, 'https://www.tsmc.com.tw/tsmcdotcom/PRListingNewsAction.do?language=C')
    print(datetime.now().strftime( "%Y-%m-%d %H:%M:%S" )) 
    t = Timer(inc, printTime, (inc,)) 
    t.start() 
# 10s
printTime( 10 )






