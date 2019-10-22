# -*- coding: utf-8 -*-
from JeuVoiture.Voiture import Voiture
from JeuVoiture.Board import Board
import os
from time import sleep
# from Dossier.Fichier import Class


"""
    Créer deux instances de la classe voiture
"""
#v1 = Voiture([2], [1])
#v1 = Voiture(6, 4)
#v2 = Voiture([4,3], [0,-1])
#print(dir(v2))

#print(v2)
#v2.avancer()
#print(v2)
#v2.tourner()
#v2.avancer()
#print(v2)

"""
    Etape 1 : Dans la classe voiture, modifier avancer() de manière à
    rester toujours entre 0 et 10 sur les deux coordonnées
    
    Etape 2 : Créer une classe Board, qui contient une liste 
    de une voiture. Cette classe une méthode run() qui fait avancer
    toute les voitures de sa liste_voitures
    self.liste_voitures = [Voiture(), Voiture()]
    
    Etape 3: ajouter une methode display à la classe Board pour aficher
    les voitures sur un board en ASCII-art (les voitures vont être
    représentées par des croix et quand il n'y a pas de voiture sur une
    case, on aura un espace)
    
    Etape 4: Ajouter la classe obstacle
            Ajouter une liste d'obstacle dans Board
            Afficher les obstacle dans display
    Etape 5: Faire en sorte que les voitures ne roulent pas
            sur les obstacles
"""

b = Board(10)

for i in range(20):
    os.system("cls")
    b.run()
    b.display()
    sleep(0.5)
