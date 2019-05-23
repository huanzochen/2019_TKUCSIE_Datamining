# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #for visualization

import seaborn as sns #for visualization

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

# We dont use plt.show() if we use "% matplotlib inline"
import os
#print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.
store = pd.read_csv("google-play-store-apps/googleplaystore.csv",usecols = [0,1,2,3,4,5,6,7,8,9,10]) 


#I dont wanna use "Current Ver" and "Android Ver" so ı use "usecols" 

print(store.info())
"""
print(store.head(100)) #quick look at the csv from first index
print(store.tail(100)) #quick look at the csv from first index
print(store.sample(6)) #random 
"""

store.columns
store.columns = store.columns.str.replace(" ","_")
print(store.columns)
print(store.dtypes)

store.Content_Rating.unique()
store.Content_Rating.value_counts().plot(kind='bar')
plt.yscale('log')
store.Genres.unique()


twowaytable = pd.crosstab(index=store["Pri_Genres"],columns=store["Sec_Genres"])
twowaytable.head()
twowaytable.plot(kind="barh", figsize=(15,15),stacked=True)

plt.legend(bbox_to_anchor=(1.0,1.0))


store.Category.value_counts().plot(kind='barh',figsize= (12,8))
#<matplotlib.axes._subplots.AxesSubplot at 0x7fd25a33b630>


"""
store.tail() #quick look at the csv from last index
store.sample(6) #random 
store.columns
store.columns = store.columns.str.replace(" ","_") #adding "_" to columns which has space.
store.dtypes
store.Size = store.Size.replace("Varies with device",np.nan)
store.Size = store.Size.str.replace("M","000")
store.Size = store.Size.str.replace("k","")
#store.Size = store.Size.apply(lambda x: float(x.replace("k",""))/1000 if "k" in x else x)
#ı wanted use this but ı get error so ı added "000" to Megabyte

store.Size = store.Size.replace("1,000+",1000)

store.Installs = store.Installs.str.replace(",","")
store.Installs = store.Installs.apply(lambda x: x.strip("+"))
store.Installs = store.Installs.replace("Free",np.nan)

store.Price = store.Price.str.replace("$","")

store = store.drop(store.index[10472])

store[["Size","Installs","Reviews","Price"]] = store[["Size","Installs","Reviews","Price"]].astype("float")
store.Category = store.Category.astype("category")
store.Installs = pd.to_numeric(store.Installs)
store.Price = pd.to_numeric(store.Price)
store = store.drop_duplicates(subset = "App", keep = "first")

store.dtypes

store.corr()

f,ax = plt.subplots(figsize = (10,10))
sns.heatmap(store.corr(), annot = True, linewidths = .5, fmt = ".2f", ax=ax)
"""


"""
#I wanna seperate free and paid apps so I can analysis objectively
free = store[store.Type == "Free"]
paid = store[store.Type == "Paid"]

store.head()
"""

"""
#We can see clearly reviews decreasing as the price increases.
paid.plot(kind = "line",x = "Price", y = "Reviews", color = "r", linestyle = ":", alpha = .5, 
          grid = True, linewidth = 1, figsize = (12,6))
plt.xlabel("Price")
plt.ylabel("Reviews")
plt.title("Paid App-Reviews")

#plt.show()
"""



"""
# We can comprasion free and paid app reviews
free.Reviews.plot(kind = "line", color = "g", linestyle = ":", alpha = .7, 
          grid = True, linewidth = 1, figsize = (12,6), label = "Free")
paid.Reviews.plot(kind = "line", color = "r", linestyle = "-.", alpha = 1, 
          grid = True, linewidth = 1, figsize = (12,6), label = "Paid")
plt.legend()
plt.xlabel("İndex")
plt.ylabel("Reviews")
plt.title("Free-Paid")
"""


#plt.show()