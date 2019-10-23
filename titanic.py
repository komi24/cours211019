#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd

df = pd.read_csv("train.csv")
df.columns
df.dtypes
df[["Survived", "Name"]]

len(df["Age"])
df.count()

df["Survived"] == 1
len(df[df["Survived"] == 1])
df[df["Survived"] == 1].count()

df["Embarked"].unique()

df.describe()
df["Embarked"].describe()


# In[8]:


df = pd.DataFrame([
    {"nom": "Bolnet", "prenom": "Mickael"},
    {"nom": "Balai", "prenom": "Michel"},
    {"nom": "Dupont", "prenom": "Mickel"},
    {"nom": "Bolneta", "prenom": "Mikael"},
    {"nom": "Bolnetb", "prenom": "Mckael"},
    {"nom": "Bolnete", "prenom": "Ckael"},
])

df.columns
df.dtypes
df["prenom"]


# In[23]:


import pandas as pd

df = pd.read_csv("train.csv")

df["Age"].hist()


# In[ ]:




