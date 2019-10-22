# -*- coding: utf-8 -*-
import numpy as np


#def assertVector(f):
#    def new_func(self, position=[0,0], direction=[1,0], marque="Renault"):
#        assert type(position) == list, "Erreur position doit être une liste"
#        assert type(direction) == list, "Erreur direction doit être une liste"
#        assert len(position) == 2, "Erreur position doit être une liste de deux éléments"
#        assert len(direction) == 2, "Erreur direction doit être une liste de deux éléments"
#        return f(self, position, direction, marque)
#    return new_func
#
#def assertVector(f):
#    def new_func(*args, **kwargs):
#        for arg in args[1:3]:
#            assert type(kwargs[k]) == list, "Erreur position doit être une liste"
#            assert len(kwargs[k]) == 2, "Erreur position doit être une liste de deux éléments"
#        for k in kwargs:
#            if k in ["position", "direction"]:
#                assert type(kwargs[k]) == list, "Erreur position doit être une liste"
#                assert len(kwargs[k]) == 2, "Erreur position doit être une liste de deux éléments"
#        return f(self, position, direction, marque)
#    return new_func


class Voiture:
    """
        Faites une classe voiture
        attributs:
            position (par défaut [0,0])
            direction (par défaut [1,0])
            marque (par défaut "Renault")
        methodes:
            avancer: Avance position += direction
            tourner: tourne la direction
    """
#    @assertVector("direction", "position")
    def __init__(self, position=[0,0], direction=[1,0], marque="Renault"):
        self.position = np.array(position)
        self.direction = np.array(direction)
        self.marque = marque
    
    def avancer(self, check_obstacle):
        new_position = self.position + self.direction
        if check_obstacle(new_position):
            self.position = new_position
        else:
            self.tourner()
            #self.avancer(check_obstacle)
        
    def tourner(self):
        self.direction = np.array([[0,1],[-1,0]]).dot(self.direction)
        
    def __str__(self):
        return str(self.position)