#!/usr/bin/env python
# coding: utf-8

# ## Introduction Python
# 
# * Les variables
# * Les boucles
# ...

# In[2]:


ma_liste = [2,1,6,8,5,12,7]

# Récupérer les 4 premiers éléments
print(ma_liste[:4])
# Récupérer les 3 derniers éléments
print(ma_liste[-3:])
# Récupérer du 2ème au 6ème (inclus) de deux en deux
print(ma_liste[1:6:2])
# Récupérer de l'avant-dernier au 3ème (sens inverse)
print(ma_liste[-2:1:-1])


# ## Loops

# In[5]:


# for i in [3,2,6]:
#     print(i)

# On itère sur les éléments d'une liste
# for elm in [True, 15, [3,6,1]]:
#     print(elm)

# print(list(range(15)))
# print(int("34") + 4)
# # print("34" + 4) # can only concatenate str (not "int") to str

ma_liste = [3,1, 6, 8,5]

for i in range(len(ma_liste)):
#     print("indice : " + str(i) +", element : " + str(ma_liste[i]))
    print(f" indice : {i}, element : {ma_liste[i]}")
    print("interieur")
    
print("extérieur")


# In[1]:


liste_ages = [ 45, 85, 62, 34 , 14, 16, 22]

i = 0
while liste_ages[i] > 18:
    print(liste_ages[i])
    i += 1


# In[7]:


age = 32
if age > 18: # != different, == egal, >= / <= 
    print("Majeur")
elif age < 18:
    print("Mineur")
else:
    print("Joyeux anniversaire")
    


# ## FizzBuzz
# 
# Afficher pour tous les entiers de 0 à 100:
# * "fizz" si l'entier est multiple de 3
# * "buzz" si l'entier est multiple de 5
# * "bazz" si l'entier est multiple de 3 et 5
# * Sinon l'entier
# 
# 

# In[ ]:




