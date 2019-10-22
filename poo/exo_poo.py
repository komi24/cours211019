# -*- coding: utf-8 -*-
from JeuVoiture.Voiture import Voiture
# from Dossier.Fichier import Class


"""
    Créer deux instances de la classe voiture
"""
#v1 = Voiture([2], [1])
v1 = Voiture(6, 4)
v2 = Voiture([4,3], [0,-1])
print(dir(v2))

print(v1)
v1.avancer()
print(v1)




