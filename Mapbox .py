#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as  go
import plotly.express as px


## Start by doing some simple statistics to get a sense of what the data looks like and the behavior of the data.


# In[72]:


## saving file path
parquet_file = r'C:\\Users\\16126\\Documents\\Python Assessment\\part-00000-c517600c-7c6a-4d83-9455-1b058c4bc1cb-c000.snappy.parquet'


# In[73]:


## importing parquet file into pandas dataframe
df = pd.read_parquet(parquet_file, engine='fastparquet')


# In[74]:


## printing first 10 rows of data 
df.head(10)


# In[12]:


## finding total number of records in data set = 
df.shape


# In[13]:


## printing solution 
r = len(df)
print ("total number of records: ", r)


# In[14]:


## total number of distinct Lat/Lon pairs 
p = len(df.groupby(['latitude', 'longitude']))
print ("number of distinct Lat/Lon pairs in dataset:", p)


# In[15]:


## viewing solution
df.groupby(['latitude', 'longitude']).size().reset_index()


# In[16]:


## number of distinct users in the dataset
n = len(pd.unique(df['ad_id']))

print("number of distinct users:", n)


# In[17]:


## viewing array of distinct users 
pd.unique(df['ad_id'])

