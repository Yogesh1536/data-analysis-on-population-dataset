#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pd.set_option('float_format', '{:f}'.format)


# In[3]:


df = pd.read_csv('world_population.csv')
df.head()


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


df.Country.unique()


# In[7]:


df.shape #dataset has 234 rows and 17 columns


# In[8]:


population_2022 = df.groupby('Country')['2022 Population'].sum().sort_values(ascending=False).head(10)
population_2022


# In[9]:


plt.rcParams['figure.figsize'] = (14,8)
plt.rcParams['axes.grid'] = True
plt.rcParams['font.size'] = 14


# In[10]:


sns.barplot(population_2022.index,population_2022.values)
plt.title('Top 10 Country with High Population in year 2022')
plt.xlabel('Country')
plt.ylabel('population')
plt.show()


# In[11]:


#top 10 country with high density
high_density = df.groupby('Country')['Density (per km²)'].sum().sort_values(ascending=False).head(10)
high_density


# In[12]:


sns.set_palette('Greens',10)
sns.barplot(high_density.index,high_density.values)
plt.title('Top 10 Countries with high density(per km^2)')
plt.xlabel('Country')
plt.ylabel('Density')


# In[13]:


growth_rate = df.groupby('Country')['Growth Rate'].sum().sort_values(ascending=False)
print("Country with highest growth rate:\n",growth_rate[:1])


# In[14]:


print("Country with highest growth rate:\n",growth_rate.tail(1))


# In[ ]:





# In[ ]:




