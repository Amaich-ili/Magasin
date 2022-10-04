"""
Iliass Amaich
Laboratoire 4
Session été 2022

"""

def menu():

    condition = True

    while condition:
        choix = input("\n(1) Afficher les Jeux de cartes "
                      "\n(2) Afficher les jeux de stratégie  "
                      "\n(3) Afficher les jeux de rôle "
                      "\n(4) Afficher les Jeux d'assemblage "
                      "\n(5) Afficher les Jeux d'adresse "
                      "\n(6) Quiter"
                      "\nVotre choix : ")

        if choix == "1" :
            pass
        elif choix == "2" :
            pass
        elif choix == "3":
            pass
        elif choix == "4":
            pass
        elif choix == "5":
            pass
        elif choix == "6" :
            condition = False

# menu()

class magasin:
    pass

class Jeu:
    def __init__(self, nom, quantite):
        self.nom = nom
        self.quantite = quantite

    def __str__(self) -> str:
        return f"Le nom de jeu est : {self.nom} \nQuantité : {self.quantite}"
           
   
class Jeu_carte(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__(nom, quantite)
       

class Jeu_strategie(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__(nom, quantite)
    

class Jeur_role(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__(nom, quantite)


class Jeu_asseblage(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__(nom, quantite)
     

class Jeu_adresse(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__(nom, quantite)
    

class tournoi:
    pass

j1 = Jeu_carte("Uno", 2)
print(j1)











