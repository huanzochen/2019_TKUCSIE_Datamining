# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:23:20 2019

@author: huang
"""

import os 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #for visualization


googleplay = pd.read_csv("google-play-store-apps/googleplaystore.csv",usecols = [0,1,2,3,4,5,6,7,8,9,10])
googleplay.Category = googleplay.Category.astype("category")
print(googleplay.head())
print(googleplay.dtypes)
print('=======')
print(googleplay.Category.value_counts()) #顯示數量
googleplay.columns = googleplay.columns.str.replace(" ","_")
googleplay.Category.value_counts().plot(kind='barh',figsize= (15,8))


