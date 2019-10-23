# -*- coding: utf-8 -*-
from .Compte import Compte


class Personne:
    def __init__(self, prenom, nom, solde_init):
        self._prenom = prenom
        self._nom = nom
        self._comptes = [Compte(solde_init)]
        
    def dire_bonjour(self):
        print(f"Bonjour, je m'appelle {self._prenom} {self._nom}. " + \
              f"J'ai {self._comptes[0].get_solde()}")
        
    def ajouter_compte(self, compte):
        self._comptes.append(compte)
        
    def transfert(self, montant, autre_personne):
        self._comptes[0].retrait(montant)
        autre_personne._comptes[0].depot(montant)
        