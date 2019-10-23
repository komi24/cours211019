# -*- coding: utf-8 -*-

class MontantNegatifException(Exception):
    pass


class SoldeInsuffisantException(Exception):
    def __init__(self, compte):
        Exception.__init__(self)
        self._compte_defaillant = compte
        
    def get_details(self):
        return str(self._compte_defaillant)


class Compte:
    def __init__(self, solde_init):
        self._solde = solde_init
    
    def retrait(self, montant):
        if montant < 0:
            raise MontantNegatifException()
        if self._solde < montant:
            raise SoldeInsuffisantException(self)
        self._solde -= montant
        
    def depot(self, montant):
        if montant < 0:
            raise MontantNegatifException()
        self._solde += montant
    
    def get_solde(self):
        return self._solde
    
    def __str__(self):
        return f"Solde : {self._solde}"
    