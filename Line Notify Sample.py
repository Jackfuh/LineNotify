# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:41:22 2019

@author: Jack
"""

import requests

def lineNotifyMessage(token, msg):
      headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
	
      payload = {'message': msg}
      r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
      return r.status_code
	
  # 修改為你要傳送的訊息內容
message = 'Yo it works: lets try 台積點最新消息'
  # 修改為你的權杖內容
token = 'CiCxIhvVem0QFKSFBbDmCWAdFmXWlVEaeR0BCMKlNjR'

lineNotifyMessage(token, message)
