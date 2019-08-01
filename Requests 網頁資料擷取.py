# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:48:55 2019

@author: Jack
"""

import requests
url = 'https://www.tsmc.com.tw/tsmcdotcom/PRListingNewsAction.do?language=E'
html = requests.get(url)
html.encoding="utf-8"
htmllist = html.text.splitlines()
n=0
for row in htmllist:
    if "Business" in row: n+=1
print("Find {} times!!!".format(n))