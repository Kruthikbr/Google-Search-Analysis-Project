#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytrends matplotlib seaborn plotly pandas


# In[2]:


import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[40]:


pytrends = TrendReq(hl='en-US', tz=360)
keyword = "cricket"


# In[41]:


pytrends.build_payload([keyword], cat=0, timeframe='today 12-m', geo='', gprop='')


# In[42]:


region_data = pytrends.interest_by_region()
region_data = region_data.sort_values(by=keyword, ascending=False).head(15)


# In[43]:


plt.figure(figsize=(10,6))
sns.barplot(x=region_data[keyword], y=region_data.index, palette='Blues_d')
plt.title(f"Top Countries Searching '{keyword}'")
plt.xlabel("Interest")
plt.ylabel("Country")
plt.show()


# In[5]:


from pytrends.request import TrendReq
import plotly.express as px

# Step 1: Set up Pytrends
pytrends = TrendReq()

# Step 2: Define your keyword
keyword = "Python"  # Change this to your keyword

# Step 3: Get interest by region data
pytrends.build_payload([keyword], timeframe='today 12-m')
region_data = pytrends.interest_by_region()

# Step 4: Reset index to make 'geoName' a column
region_data = region_data.reset_index()

# Step 5: Plot Choropleth Map
fig = px.choropleth(
    region_data,
    locations='geoName',
    locationmode='country names',
    color=keyword,
    title=f"Search Interest for '{keyword}' by Country",
    color_continuous_scale='Blues'
)

fig.show()


# In[45]:


time_df = pytrends.interest_over_time()


# In[46]:


plt.figure(figsize=(12,6))
plt.plot(time_df.index, time_df[keyword], marker='o', color='purple')
plt.title(f"Search Interest Over Time for '{keyword}'")
plt.xlabel("Date")
plt.ylabel("Interest")
plt.grid(True)
plt.xticks(rotation=45)


# In[26]:


kw_list = ["cloud computing", "data science", "machine learning"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='')


# In[15]:


compare_df = pytrends.interest_over_time()
plt.figure(figsize=(12,6))
for kw in kw_list:
 plt.plot(compare_df.index, compare_df[kw], label=kw)
plt.title("Keyword Comparison Over Time")
plt.xlabel("Date")
plt.ylabel("Search Interest")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:




