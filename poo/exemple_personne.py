# -*- coding: utf-8 -*-
from PckgPersonne.Compte import Compte, SoldeInsuffisantException, MontantNegatifException
from PckgPersonne.Personne import Personne

"""
    Compte:
        attribut:
            - _solde
        methode:
            - depot(montant)
            - retrait(montant)
            - get_solde()
            
    Personne:
        attributs:
            - nom
            - prenom
            - compte
        methode:
            - dire_bonjour : "Bonjour, je m'appelle {nom} {prenom}"
            - transfert(montant, autre_personne)
"""

une_personne = Personne("Maxence", "Bouret", 10000)
autre_personne = Personne("Yacine", "Hmito", 5000)

try:
    une_personne.transfert(200000, autre_personne)
    
    une_personne.dire_bonjour()
    autre_personne.dire_bonjour()
except SoldeInsuffisantException as e:
    print("Le solde est insuffisant")
    print(e.get_details())
except MontantNegatifException:
    print("Le montant est négatif")
except:
    print("Une autre erreur est survenue")


