# -*- coding: utf-8 -*-

import os
from time import sleep
from .Voiture import Voiture
from random import randint as rd
from random import choice


#os.system("clear")
#os.system("cls")
#
#sleep(0.5)
#
def get_random_position():
    return [rd(0,10), rd(0,10)]

def get_random_direction():
    return choice([[1,0],[-1,0],[0,-1],[0,1]])

class Board:
    def __init__(self, nb_voiture=4):
        self.liste_voitures = [
                Voiture(get_random_position(), get_random_direction())
                for i in range(nb_voiture)]
    
    def run(self):
        for voiture in self.liste_voitures:
            voiture.avancer()
            
    def display(self):
        for i in range(11):
            ligne = []
            for j in range(11):
                if self._is_voiture([i,j]):
                    ligne.append('x')
                else:
                    ligne.append(' ')
            print(ligne)
        
    def _is_voiture(self, position):
        for voit in self.liste_voitures:
            if (voit.position == position).all():
                return True
        return False
    
    
    
    