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

# ## https://github.com/komi24/cours211019

# In[10]:


for i in range(101):
    if i % 5 == 0 and i % 3 == 0: # i % 15 == 0
        print("bazz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)


# In[1]:


# On importe la fonction randint de la librairie random
from random import randint as rd

# import random
# random.randint(0,100)

secret = rd(0,100)
proposition_utilisateur = None

while proposition_utilisateur != secret:
    proposition_utilisateur = int(input("Quelle est votre proposition ?"))
    if proposition_utilisateur < secret:
        print("trop petit")
    elif proposition_utilisateur > secret:
        print("trop grand")
    else:
        print("Gagné")


# In[4]:


borne_min = 0
borne_max = 101

reponse_utilisateur = None

while reponse_utilisateur != "E": 
    proposition = (borne_min + borne_max) // 2
    reponse_utilisateur = input(f"Est-ce que le secret est {proposition} ? P/G/E")
    if reponse_utilisateur == "P":
        borne_max = proposition
    elif reponse_utilisateur == "G":
        borne_min = proposition

print("Bien joué")


# ## Comprehensive list et ternaires 

# In[8]:


liste_ages = [32,53,12,8,36]

par2 = [elm * 2 for elm in liste_ages]
print(par2)

restes = [elm % 2 == 0 for elm in liste_ages]
print(restes)

majeurs = [elm for elm in liste_ages if elm * 2 >= 100]
print(majeurs)


# In[9]:


age = 36

etat = "majeur" if age >= 18 else "mineur"
print(etat)


# ## Les fonctions

# In[11]:


# Définition d'une fonction
def dire_bonjour():
    print("Bonjour tout le monde")

# Utilisation d'une fonction
dire_bonjour()
# Utilisation d'une fonction
dire_bonjour()


# In[12]:


def dire_bonjour(nom):
    return f"Bonjour {nom}"

resultat = dire_bonjour("Mathieu")
print(resultat)


# In[14]:


def dire_bonjour(nom, nom2, nom3):
    return f"Bonjour {nom} {nom2} {nom3}"

resultat = dire_bonjour("Mathieu", "Elise", "Gerard")
print(resultat)


# In[20]:


def dire_bonjour(nom, nom2="", nom3="", age=15):
    print(f"nom2 : {nom2}")
    print(f"nom3 : {nom3}")
    return f"Bonjour {nom} {nom2} {nom3}", age

resultat, age = dire_bonjour("Mathieu", "Elise", "Gerard")
print(resultat)
resultat, age = dire_bonjour("Mathieu")
print(resultat)
resultat, age = dire_bonjour("Mathieu", "Helene")
print(resultat)
resultat, age = dire_bonjour("Mathieu", nom3="Helene")
print(resultat)
print(age)


# In[29]:


personne = {
    "nom": "Dupont",
    "prenom": "Martin",
    "age": 37,
    "liste_matieres": ["SVT", "Maths", "EPS"],
    True: dire_bonjour
}

print(personne["nom"])
print(personne["prenom"])
print(personne["liste_matieres"][-1])

personne[True]("Martin")

liste_prenoms = ["Martin", "Laurent", "Eloise", "Eugenie"]

liste_personnes = [{
    "nom": "Dupont",
    "prenom": prenom
} for prenom in liste_prenoms]

print(liste_personnes)


# In[27]:


def dire_bonjour_en():
    print("Hello world")
def dire_bonjour_fr():
    print("Bonjour")
def dire_bonjour_es():
    print("Hola")
def dire_bonjour_pt():
    print("Oi")
def dire_bonjour_zh():
    print("Ni hao")

langues = {
    "EN": dire_bonjour_en,
    "FR": dire_bonjour_fr,
    "ES": dire_bonjour_es,
    "PT": dire_bonjour_pt,
    "ZH": dire_bonjour_zh,
}

lng = input(f"Quel est votre langue ?")
langues[lng]()


# In[30]:


liste_prenoms = ["Martin", "Laurent", "Eloise", "Eugenie"]
liste_ages = [45, 58, 23]

liste_personnes = [{
    "nom": "Dupont",
    "prenom": prenom,
    "age": age
} for prenom, age in zip(liste_prenoms, liste_ages)]

print(liste_personnes)


# In[31]:


for i, prenom in enumerate(liste_prenoms):
    print(f"Le {i}eme prenom est {prenom}")


# In[32]:


equipeA = ["John", "Elie", "Enora"]
equipeB = ["Mathis", "Maud", "Yael"]

from itertools import product 

for eA, eB in product(equipeA, equipeB):
    print(f"{eA} vs {eB}")


# In[ ]:


# Faite une fonction dire bonjour 
# Qui retourne "bonjour {nom}" si le parametre lng est "FR"
# Qui retourne "Hello {nom}" si le parametre lng est "EN"
# Par défaut lng = "FR"

