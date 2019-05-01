#!/usr/bin/env python
# coding: utf-8

# ## 練習時間
# 在小量的資料上，我們用眼睛就可以看得出來程式碼是否有跑出我們理想中的結果
# 
# 請嘗試想像一個你需要的資料結構 (裡面的值可以是隨機的)，然後用上述的方法把它變成 pandas DataFrame
# 
# #### Ex: 想像一個 dataframe 有兩個欄位，一個是國家，一個是人口，求人口數最多的國家
# 
# ### Hints: [隨機產生數值](https://blog.csdn.net/christianashannon/article/details/78867204)

# In[1]:


import pandas as pd
import numpy as np


# In[26]:


data = {'國家':['TAIWAN', 'UNITED states', 'Thai'] ,
        '人口':[139, 237, 126] }
#data = pd.DataFrame()


# In[27]:


Countrylist = pd.DataFrame(data)
print(Countrylist)


# In[ ]:


import random
def random_list(start,stop,length):
    if length>=0:
        length=int(length)

