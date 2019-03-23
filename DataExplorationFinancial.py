#!/usr/bin/env python
# coding: utf-8

# # Setup

# In[201]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid
import os

DATA_DIR = 'data'
FINANCIAL_DIR = os.path.join(DATA_DIR, 'financial')


# In[202]:


def load_data_frame(file_name, path):
    """
    Loads data from specified path and returns adata frame.
    """
    file_path = os.path.join(path, file_name)
    return pd.read_csv(file_path)


# ## Unemployment Rate Data By Country

# In[260]:


unemployment_df = load_data_frame('unemploymentrate.csv', FINANCIAL_DIR)

unemployment_df.columns = unemployment_df.iloc[1].tolist() #set the header row as the df header
unemployment_df = unemployment_df[2:] #take the data less the header row

#rename the country column
unemployment_df.rename(columns={ unemployment_df.columns[0]: "country" }, inplace = True)

#replace non-numericals
unemployment_df = unemployment_df.replace('..', np.NaN)

# convert all columns of DataFrame to numeric
unemployment_df.loc[:,1:] = unemployment_df.iloc[:,1:].apply(pd.to_numeric)
unemployment_df.head()

#select the webscraped countries to graph
#selected_data = unemployment_df.loc[unemployment_df['country'].isin(selected_countries)].T

unemployed_t = unemployment_df.T

fig = plt.figure(figsize=(50,20))
ax = fig.add_subplot(1,1,1)
ax.plot(unemployed_t[1:])
ax.set(title='Unemployment rate by country from 1990-2016',
 ylabel='Unemployment', xlabel='Year')
plt.show()


# ## GDP Data By Country

# In[261]:


#Load GDP information
gdp_df = load_data_frame('GDP.csv', FINANCIAL_DIR)
gdp_df.rename(columns={ gdp_df.columns[0]: "country" }, inplace = True)

#replace non-numericals and drop all nan rows
gdp_df = gdp_df.replace('..', np.NaN)

# convert all columns of DataFrame to numeric
gdp_df.loc[:,1:] = gdp_df.iloc[:,1:].apply(pd.to_numeric)

#this file also contains GDP information that is based on other statistics. We remove them
gdp_df = gdp_df.drop_duplicates('country')

gdp_t = gdp_df.T

fig = plt.figure(figsize=(50,20))
ax = fig.add_subplot(1,1,1)
ax.plot(gdp_t[1:])
ax.set(title='GDP by country from 1990-2016, index 2010=100',
 ylabel='GDP', xlabel='Year')
plt.show()


# In[ ]:




