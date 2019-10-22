# -*- coding: utf-8 -*-

def decorateur(f):
    print("décoration")
    def nouvelle_fonction(name):
        assert type(name) == str, "Erreur, votre param doit être une string"
        return f(name)
    return nouvelle_fonction


@decorateur
def dire_bonjour(name):
    print(f"Bonjour {name}")
    

dire_bonjour("Toto")
dire_bonjour("Toto")
dire_bonjour("Toto")
dire_bonjour(2)