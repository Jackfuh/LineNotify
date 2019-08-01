# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:09:02 2019

@author: Jack
"""

import hashlib, os, requests
#讀取網頁原始碼
url = 'http://opendata.epa.gov.tw/webapi/Data/ATM00625/?$skip=0&$top=1000&format=json'
html = requests.get(url).text.encode("utf-8-sig")
#判斷網頁是否更新
old_md5=""
md5 = hashlib.md5(html).hexdigest()
if os.path.exists('old_md5.txt'):
    with open('old_md5.txt', 'r') as f:
        old_md5 = f.read()
    with open('old_md5.txt', 'w') as f:
        f.write(md5)
else:
    with open('old_md5.txt', 'w') as f:
        f.write(md5)
        
if md5 != old_md5:
    print('資料已更新與網站同步...')
    
else:
    print('網站資料未更新...')