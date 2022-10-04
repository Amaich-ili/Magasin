"""
Iliass Amaich
Laboratoire 4
Session été 2022

"""

def menu():
    magasin = Magasin()
    condition = True

    while condition:
        choix = input("\n(1). Afficher les Jeux de cartes "
                      "\n(2). Afficher les jeux de stratégie  "
                      "\n(3). Afficher les jeux de rôle "
                      "\n(4). Afficher les Jeux d'assemblage "
                      "\n(5). Afficher les Jeux d'adresse "
                      "\n(6). Quiter"
                      "\nVotre choix : ")

        if choix == "1":
            print(magasin.Jeu_carte())
        elif choix == "2":
            print(Jeu_strategie())
        elif choix == "3":
            print(Jeur_role())
        elif choix == "4":
            print(Jeu_asseblage())
        elif choix == "5":
            print(Jeu_adresse())
        elif choix == "6":
            condition = False


# menu()

class Magasin:
    def __init__(self):
        self.liste_jeu = []
        with open("fichier.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                objet = line.split()

                # if objet[0] == "Uno":
                #     self.liste_jeu.append(Jeu_carte(objet[0], objet[1]))
                # elif objet[0] == "Solitaire":
                #     self.liste_jeu.append(Jeu_carte(objet[0], objet[1]))
                # elif objet[0] == "Elvenar":
                #     self.liste_jeu.append(Jeu_strategie(objet[0], objet[1]))
                # elif objet[0] == "Grepolis":
                #     self.liste_jeu.append(Jeu_strategie(objet[0], objet[1]))
                # elif objet[0] == "malefices":
                #     self.liste_jeu.append(Jeur_role(objet[0], objet[1]))
                # elif objet[0] == "Kuro":
                #     self.liste_jeu.append(Jeur_role(objet[0], objet[1]))
                # elif objet[0] == "Casse_tete":
                #     self.liste_jeu.append(Jeu_asseblage(objet[0], objet[1]))
                # elif objet[0] == "Rubik's_cube":
                #     self.liste_jeu.append(Jeu_asseblage(objet[0], objet[1]))
                # elif objet[0] == "Monopolie":
                #     self.liste_jeu.append(Jeu_adresse(objet[0], objet[1]))
                # elif objet[0] == "mahjong":
                #     self.liste_jeu.append(Jeu_adresse(objet[0], objet[1]))

                if objet[0] == "Jeu_carte":
                    self.liste_jeu.append(Jeu_asseblage(objet[1], objet[2]))
                elif objet[0] == "Jeu_strategie":
                    self.liste_jeu.append(Jeu_strategie(objet[1], objet[2]))
                elif objet[0] == "Jeur_role":
                    self.liste_jeu.append(Jeur_role(objet[1], objet[2]))
                elif objet[0] == "Jeu_asseblage":
                    self.liste_jeu.append(Jeu_asseblage(objet[1], objet[2]))
                elif objet[0] == "Jeu_adresse":
                    self.liste_jeu.append(Jeu_adresse(objet[1], objet[2]))

        for objet in self.liste_jeu:
            print(objet)


class Jeu:
    def __init__(self, nom, quantite):
        self.nom = nom
        self.quantite = quantite

    def __str__(self) -> str:
        return f"Le nom de jeu est : {self.nom} \nQuantité : {self.quantite}"


class Jeu_carte(Jeu):
    def __init__(self, nom, quantite):
        super().__init__(nom, quantite)


class Jeu_strategie(Jeu):
    def __init__(self, nom, quantite):
        super().__init__(nom, quantite)


class Jeur_role(Jeu):
    def __init__(self, nom, quantite):
        super().__init__(nom, quantite)


class Jeu_asseblage(Jeu):
    def __init__(self, nom, quantite):
        super().__init__(nom, quantite)


class Jeu_adresse(Jeu):
    def __init__(self, nom, quantite):
        super().__init__(nom, quantite)


class tournoi:
    pass


# j1 = Jeu_carte("Uno", 2)
# print(j1)
m = Magasin()





















