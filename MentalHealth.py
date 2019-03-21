#!/usr/bin/env python
# coding: utf-8

# # Data Exploration
# <br/>
# In this notebook you will find work on data preprocessing and amalgamation of mental health data different sources.
# <br/>
# Ensure required data is available in the [data/mental_health] directory.
# 
# 

# ## Setup

# In[73]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import matplotlib.gridspec as grid
import numpy as np
import os
import pandas

DATA_DIR = 'data'
MENTAL_HEALTH_DIR = os.path.join(DATA_DIR, 'mental_health')


# In[10]:


def load_data_frame(file_name, path):
    """
    Loads data from specified path and name, returns a dataframe 
    """

    file_path = os.path.join(path, file_name)
    return pandas.read_csv(file_path)


mental_df = load_data_frame(
    'prevalence-by-mental-and-substance-use-disorder.csv',
    MENTAL_HEALTH_DIR
)
mental_df.info()


# In[66]:


mental_df.columns.tolist()


# In[17]:


mental_df.head(10)


# In[53]:


non_country_entities = [
    'Andean Latin America', 'Central Asia', 'Central Europe',
    'Central Latin America', 'Central Sub-Saharan Africa',
    'East Asia', 'Eastern Europe', 'Eastern Sub-Saharan Africa',
    'High SDI', 'High-income Asia Pacific', 'High-middle SDI',
    'Latin America and Caribbean', 'Low SDI', 'Low-middle SDI',
    'Middle SDI', 'North Africa and Middle East', 'North America',
    'Oceania', 'South Asia', 'Southeast Asia', 'Southern Latin America',
    'Southern Sub-Saharan Africa', 'Sub-Saharan Africa', 'Tropical Latin America', 
    'Western Europe', 'Western Sub-Saharan Africa', 'World',
]

mental_df = mental_df[~mental_df['Entity'].isin(non_country_entities)]


# ### Disorder Rate by Country (per annum)

# In[78]:


fig, axes = plt.subplots(nrows=7, sharex=True, figsize=(40,90))
gr = grid.GridSpec(7, 1)
gr.update(hspace=0.001)


alpha = 0.4
targets = mental_df.columns.tolist()

for year in mental_df['Year'].unique():
    x = mental_df.loc[mental_df['Year'] == year, 'Entity']

    for i, ax in enumerate(axes):
        y = mental_df.loc[mental_df['Year'] == year, targets[3+i]],
        ax.set_title(targets[3+i], fontsize=20)
        ax.scatter(
            x,
            y,
            alpha=alpha,
            label=year,
        )


plt.xticks(rotation=90)
plt.margins(x=0)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


# In[ ]:




