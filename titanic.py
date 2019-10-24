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


# In[42]:


total = len(df)
# Nombre de femmes
nb_femmes = len(df[(df["Sex"] == "female")])
# Nombre d'hommes
nb_hommes = len(df[(df["Sex"] == "male")])
# Proportion de femmes sur le bateau
p_femmes = nb_femmes / total
# Proportion de femmes qui ont survécu
p_f_s = len(df[(df["Sex"] == "female") & (df["Survived"] == 1)]) / nb_femmes
# Proportion d'hommes qui ont survécu
p_h_s = len(df[(df["Sex"] == "male") & (df["Survived"] == 1)]) / nb_hommes


print(f"""
    nombre de femmes : {nb_femmes}
    nombre de hommes : {nb_hommes}
    propostion de femmes : {p_femmes}
    propostion de femmes qui ont survécu : {p_f_s}
    propostion de femmes qui ont survécu : {p_h_s}
""")

# histogramme des Ages des survivants
df["Age"].hist()
df[df["Survived"] == 1]["Age"].hist()


# In[36]:


df["Fare"].sort_values().reset_index()["Fare"].plot()


# In[37]:


df.plot.scatter("Age", "Fare")


# In[85]:


import pandas as pd

df = pd.read_csv("train.csv")
df.describe()
df.count()
df.drop(columns=["Cabin", "Ticket"], inplace=True)
df.count()
df.dtypes
df["Sex"] = df["Sex"].map({"female": 1, "male": 0})
df.dtypes
# Transformez Embarked en integer
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
df.Name

def extract_title(name):
    return re.findall(", ([^.]*)\.", name)[0]

df["Title"] = df["Name"].map(extract_title)

titles = list(df.Title.unique())

df.Title = df.Title.map(lambda t : titles.index(t))
df.drop(columns=["Name"], inplace=True)
df.dropna(inplace=True)


# In[54]:


df["Age"] + df["Fare"] * df["Age"] + df["Sex"]

df.eval("Age + Fare * Age + Sex")


# In[73]:


# Si la comptesse a survécu
df[df["Title"] == "the Countess"]
# Si la capitaine a survécu
df[df["Title"] == "Capt"]


# In[86]:


df.count()


# In[ ]:




