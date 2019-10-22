#from . import LNG_DEFAULT


def dire_bonjour(name: str, lng="FR"):
    if lng == "EN":
        dire_bonjour_en(name)
    if lng == "ES":
        dire_bonjour_es(name)
    if lng == "FR":
        dire_bonjour_fr(name)
    
def dire_bonjour_en(name):
    print(f"Hello {name}")

def dire_bonjour_es(name):
    print(f"Hola {name}")

def dire_bonjour_fr(name):
    print(f"v2 Bonjour {name}")


print(__name__)
if __name__ == "__main__":
    dire_bonjour("Toto")








