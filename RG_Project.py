#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries & Datasets

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_excel("Data_Project.xlsx")


# In[3]:


data.head()


# # Missing Value Treatment

# In[4]:


data.isna().sum()


# In[5]:


data.drop('ta_fights', axis = 1, inplace = True)
data.drop('ltv', axis = 1, inplace = True)


# In[6]:


data.isna().sum()


# In[7]:


data['robots_owned'].value_counts()


# In[8]:


data['robots_owned'].fillna(data['robots_owned'].mode()[0], inplace = True)
data['ch_fights'].fillna(data['ch_fights'].mode()[0], inplace = True)
data['fs_fights'].fillna(data['fs_fights'].mode()[0], inplace = True)
data['last_fight_index'].fillna(data['last_fight_index'].mode()[0], inplace = True)


# In[9]:


data.isna().sum()


# In[10]:


data.dropna(inplace = True)


# In[11]:


data.shape


# In[92]:


data.columns


# # Univariate Analysis

# ## Description

# In[94]:


data.describe()


# ## Pie Plot of Last Fight Name

# In[113]:


plt.pie(data['last_ch_fightname'].value_counts(), labels = data['last_ch_fightname'].value_counts().keys())
plt.show()


# In[ ]:





# In[ ]:





# # Bivariate Analysis

# ## Correlation Plot

# In[95]:


data.corr()


# In[97]:


plt.figure(figsize = (15,7))
sns.heatmap(data.corr(), cmap = 'viridis', annot = True)


# ## Linear Plot

# In[131]:


sns.set_theme(color_codes=True)
sns.lmplot(x = 'sessions', y = 'session_length', data = data)


# - From the Linear Plot, it is evident that Sessions & Session Length are not linearly related.

# # Visualize

# ## Robots Owned vs Total Playtime

# In[55]:


plt.figure(figsize = (15,7))
plt.scatter(x = 'robots_owned', y = 'total_playtime', data = data)
plt.show()


# - People who own 0 to 10 Robots are bound to play for more sessions leading to more playtime duration.

# In[56]:


def function_1(x):
    if 0 < x < 101:
        return "0-100 Minutes"
    elif 100 < x < 201:
        return "101-200 Minutes"
    elif 200 < x < 301:
        return "201-300 Minutes"
    elif 300 < x < 401:
        return "301-400 Minutes"
    else:
        return "Above 400 Minutes"
    
data['total_playtime_range'] = data['total_playtime'].apply(function_1)


# In[61]:


a = data['total_playtime_range'].value_counts().keys()
b = data['total_playtime_range'].value_counts().values


# In[65]:


plt.figure(figsize = (15,7))
sns.set_style(style = 'whitegrid')
sns.countplot(x = data['total_playtime_range'])


# - The most common play timings is on an average of 100 Minutes.

# In[71]:


def function_2(x):
    if 0 < x < 3:
        return "2 Robots Owned"
    elif 2 < x < 6:
        return "3 to 5 Robots Owned"
    elif 5 < x < 9:
        return "6 to 8 Robots Owned"
    elif 8 < x < 12:
        return "9 to 11 Robots Owned"
    elif 11 < x < 15:
        return "12 to 14 Robots Owned"
    else:
        return "Above 14 Robots Owned"
    
data['robots_owned_range'] = data['robots_owned'].apply(function_2)


# In[72]:


plt.figure(figsize = (15,7))
sns.set_style(style = 'whitegrid')
sns.countplot(x = 'robots_owned_range', data = data)


# - Majority of the Players owned 2 Robots.

# ## Game Mode v/s Robots Owned

# In[73]:


data.columns


# In[77]:


data['fs_fights']


# In[86]:


data['robots_owned'].value_counts()


# ### Championship Fight Mode

# In[90]:


plt.figure(figsize = (15,7))
plt.scatter(x = 'ch_fights', y = 'robots_owned', data = data)
plt.show()


# ### Free Sparing Fight Mode 

# In[91]:


plt.figure(figsize = (15,7))
plt.scatter(x = 'fs_fights', y = 'robots_owned', data = data)
plt.show()


# In[ ]:




