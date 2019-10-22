# -*- coding: utf-8 -*-


class Personne:
    """
        Une classe pour les personnes
    """
    def __init__(self, prenom, nom, age=34):
        """
            Constructeur
            :param prenom: prenom de la personne
            :param nom: nom de la personne
            :param age: age de la personne
        """
        self.prenom = prenom
        self.nom = nom
        self.age = age
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
    def __eq__(self, autre_personne):
        return self.prenom == autre_personne.prenom and \
            self.nom == autre_personne.nom
    
une_personne = Personne("Jutsine", "Jung")
une_autre_personne = Personne("Roger", "Koskas", 56)
une_trois_personne = Personne("Roger", "Koskas", 65)

#une_personne.prenom = "Roger"

print(une_personne.prenom)
print(une_autre_personne.prenom)
print(une_personne.age)
print(une_autre_personne.age)

print(une_personne)

print(une_autre_personne == une_trois_personne)
help(Personne)


import numpy as np
help(np.ndarray)
print(type(np.array([2,2])))