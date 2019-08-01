# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:56:27 2019

@author: Jack
"""

from datetime import datetime 
from threading import Timer 
#打印時間函數
def printTime (inc) :
    print(datetime.now().strftime( "%Y-%m-%d %H:%M:%S" )) 
    t = Timer(inc, printTime, (inc,)) 
    t.start() 
# 5s
printTime( 5 )