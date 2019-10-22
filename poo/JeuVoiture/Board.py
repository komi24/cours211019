# -*- coding: utf-8 -*-

import os
from time import sleep
from .Voiture import Voiture
from .Obstacle import Obstacle
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
    def __init__(self, nb_voiture=4, nb_obstacles=6):
        self.liste_voitures = [
                Voiture(get_random_position(), get_random_direction())
                for i in range(nb_voiture)]
        self.liste_obstacles = [
                Obstacle(get_random_position())
                for i in range(nb_obstacles)]
    
    def run(self):
        for voiture in self.liste_voitures:
            voiture.avancer(self._is_available)
            
    def display(self):
        for i in range(11):
            ligne = []
            for j in range(11):
                if self._is_voiture([i,j]):
                    ligne.append('x')
                elif self._is_obstacle([i,j]):
                    ligne.append('o')
                else:
                    ligne.append(' ')
            print("".join(ligne))
        
    def _is_voiture(self, position):
        for voit in self.liste_voitures:
            if (voit.position == position).all():
                return True
        return False

    def _is_obstacle(self, position):
        for obs in self.liste_obstacles:
            if (obs.position == position).all():
                return True
        return False
    
    def _is_available(self, position):
        """
            return True si la case en position est disponible
            (pas d'obstacle)
        """
        if not ((position <= 10).all() and (position >= 0).all())   :
            return False
        return (not self._is_obstacle(position)) and \
            (not self._is_voiture(position))
    
    
    