# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:19:54 2019

@author: huang
"""
import os
from sklearn import datasets  
import pandas as pd
iris = datasets.load_iris()    #導入鳶尾花資料集
x = pd.DataFrame(iris['data'],columns=iris['feature_names']) #這裡的特徵是花瓣的長寬
print(x)
#os.system("pause")