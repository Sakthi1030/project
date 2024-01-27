#!/usr/bin/env python
# coding: utf-8

# In[63]:     
import pandas as pd 
from pandas import ExcelWriter 
from pandas import ExcelFile 
titanic_df = pd.read_excel('titanic3.xls')
wine_df = pd.read_csv('wine.csv')
brain_df = pd.read_csv('brain_size.csv',sep = ';')
from sklearn import preprocessing as pp
titanic_df['fare'].head()

# In[64]:
data_scalar = pp.MinMaxScaler(feature_range = (0,1))
fare_away = titanic_df[['fare']]
fare_away

# In[65]:
fare_away_sealed = data_scalar.fit_transform(fare_away)
fare_away_sealed

# In[66]:
titanic_df['fare_away_sealed'] = fare_away_sealed
titanic_df

# In[67]:
titanic_df.info()

# In[68]:
col_to_drop = ['body','boat','cabin','name']
titanic_df = titanic_df.drop(col_to_drop,axis = 1)
titanic_df.info()

# In[69]:
titanic_df['age'] = titanic_df['age'].interpolate()
titanic_df.info()

# In[70]:
titanic_df = titanic_df.dropna()
titanic_df

# In[71]:
brain_df
normalizer = pp.Normalizer(norm = 'l1')
fisq_array = brain_df[['FSIQ']]
fisq_array_norm = normalizer.transform(fisq_array)
brain_df['FISQ_normalized'] = fisq_array_norm
brain_df

# In[72]:
brain_df.info()

# In[73]:
brain_df.loc[brain_df['Gender']== 'Male','Gender'] = 1
brain_df.loc[brain_df['Gender']== 'Female','Gender'] = 0
brain_df

# In[74]:
bins = pp.Binarizer(threshold = 100)
VIQ_array = brain_df[['VIQ']].values
bins.fit(VIQ_array)

# In[75]:
y = titanic_df[['survived']]
x= titanic_df.drop(columns= 'survived',axis =1)
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
x,y = make_blobs(n_samples = 1000)

# In[76]:
x

# In[77]:
y

# In[80]:
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=30)
print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)




