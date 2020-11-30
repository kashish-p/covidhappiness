#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

print('Modules are imported.')


# In[5]:


corona_dataset_csv = pd.read_csv('Datasets/covid19_Confirmed_dataset.csv')
corona_dataset_csv.head(10)


# In[6]:


corona_dataset_csv.shape


# In[12]:


corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)


# In[13]:


corona_dataset_csv.head(10)


# In[15]:


corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()


# In[16]:


corona_dataset_aggregated.head(10)


# In[17]:


corona_dataset_aggregated.shape


# In[18]:


corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['Italy'].plot()
corona_dataset_aggregated.loc['Spain'].plot()
plt.legend()


# In[19]:


corona_dataset_aggregated.loc['China'].plot()


# In[20]:


corona_dataset_aggregated.loc['China'].diff().plot()


# In[21]:


countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max infection rate'] = max_infection_rates


# In[22]:


corona_dataset_aggregated.head()


# In[23]:


corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])


# In[24]:


corona_data.head()


# In[25]:


world_happiness_report = pd.read_csv("Datasets/2020_report.csv")
world_happiness_report.head()


# In[26]:


world_happiness_report.shape


# In[27]:


columns_to_dropped = ['Overall rank','Score','Generosity','Perceptions of corruption']
world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)


# In[32]:


world_happiness_report.head()


# In[39]:


columns_to_dropped = ['happiness_score','generosity','government_trust', 'dystopia_residual', 'continent']
world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)


# In[40]:


world_happiness_report.head()


# In[43]:


world_happiness_report.set_index(['country'],inplace=True)
world_happiness_report.head()


# In[44]:


corona_data.head()


# In[45]:


world_happiness_report.head()


# In[46]:


data = world_happiness_report.join(corona_data).copy()
data.head()


# In[47]:


data.corr()


# In[48]:


data.head()


# In[50]:


x = data['gdp_per_capita']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))


# In[51]:


sns.regplot(x,np.log(y))


# In[52]:


x = data['health']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))


# In[53]:


sns.regplot(x,np.log(y))


# In[55]:


x = data['freedom']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))


# In[56]:


sns.regplot(x,np.log(y))

