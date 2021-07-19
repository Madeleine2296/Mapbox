#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as  go
import plotly.express as px

## start to visualize data.  The first geograph is a visualization of 50K rows of the data set.
## The second visualization is taking 3 different devices and tracking their lat/lon


# In[2]:


parquet_file = r'C:\\Users\\16126\\Documents\\Python Assessment\\part-00000-c517600c-7c6a-4d83-9455-1b058c4bc1cb-c000.snappy.parquet'


# In[3]:


df = pd.read_parquet(parquet_file, engine='fastparquet')


# In[4]:


## setting mapbox access token 
px.set_mapbox_access_token('pk.eyJ1IjoiaG9tbTg5ODIiLCJhIjoiY2twdWo2cXZqMHJtazJvcXYxMmJvZnJjZCJ9.s97bbsehFDs9sDpyfPQyqg')


# In[35]:


## visualize the movement data by taking 50K rows 
fig = px.scatter_mapbox(df[:50000], lat="latitude", lon="longitude",
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)


# In[36]:


fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[46]:


## grouping the devices
devices = df.groupby('ad_id').count().reset_index()


# In[47]:


## displaying 10 rows of devices and their corresponding lat/lon
devices[:10].value_counts().reset_index()


# In[54]:


devices[:3]


# In[50]:


fig2 = px.line_mapbox(devices[:3], lat="latitude", lon="longitude", color="ad_id", zoom=1, height=300)


# In[52]:


fig2.update_layout(mapbox_style="open-street-map", mapbox_zoom=4, mapbox_center_lat = 41,
    margin={"r":0,"t":0,"l":0,"b":0})
fig2.show()


# In[ ]:




