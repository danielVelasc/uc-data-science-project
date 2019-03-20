#!/usr/bin/env python
# coding: utf-8

# ## News Headline Scraping

# In[16]:


# Imports for web scraping

from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

# Google news URL
URL = 'https://news.google.com/search?q=+when:1y&gl='

# List of countries to retrieve headline data for
# [Canada, United States, Great Britain]
countries = ['CA', 'US', 'GB']


# In[17]:


headlines_df = pd.DataFrame()

for country in countries:
    news_link = URL + country
    
    response = requests.get(news_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headlines = [l.get_text() for l in soup.find_all('a', class_="DY5T1d")]
    
    headlines_df = pd.concat([headlines_df, pd.DataFrame({ country: headlines })], axis=1) 


# In[19]:


headlines_df.head(100)

