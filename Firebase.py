# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:35:17 2019

@author: Jack
"""

from firebase import firebase
url = 'https://pythonfirebase-71caf.firebaseio.com/'
fb = firebase.FirebaseApplication(url, None)
fb.post('/test', "Pythontest")
