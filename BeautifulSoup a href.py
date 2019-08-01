# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:51:53 2019

@author: Jack
"""

from bs4 import BeautifulSoup
import requests
url = 'https://www.tsmc.com.tw/tsmcdotcom/PRListingNewsAction.do?language=E'
html = requests.get(url)
html.encoding="utf-8"

sp = BeautifulSoup(html.text, "html.parser")
links = sp.find_all(["a","img"]) #同時讀取 <a> 和 <img>

for link in links:
    href=link.get("href") #讀取href內容
    if href!= None and href.startswith("http://"):
        print(href)