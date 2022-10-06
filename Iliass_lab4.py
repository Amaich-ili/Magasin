"""
Iliass Amaich
Laboratoire 4
Session été 2022

"""

class Magasin:
    def __init__(self):
        self.liste_objet = []
        self.choix = ""
        self.qtt = int
        self.dict_jeu = {
                        "Uno": Uno, "Solitaire" : Solitaire, "Elvenar": Elvenar, 
                        "Grepolis": Grepolis, "Malefices":Malefices, "Kuro": Kuro,
                        "Casse_tete": Casse_tete, "Rubik's_cube": Rubiks_cube,
                        "Monopolie": Monopolie, "Mahjong": Mahjong
                        }
        
        with open("fichier.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                objet = line.split()
                #constructeurs = {"jeu_carte": Jeu_carte, ...}
                #constructeurs[user_input](int(objet[2]))
                if objet[0] == "Jeu_carte":
                    self.liste_objet.append(Jeu_carte(objet[1], int(objet[2])))
                elif objet[0] == "Jeu_strategie":
                    self.liste_objet.append(Jeu_strategie(objet[1], int(objet[2])))
                elif objet[0] == "Jeur_role":
                    self.liste_objet.append(Jeur_role(objet[1], int(objet[2])))
                elif objet[0] == "Jeu_assemblage":
                    self.liste_objet.append(Jeu_assemblage(objet[1], int(objet[2])))
                elif objet[0] == "Jeu_adresse":
                    self.liste_objet.append(Jeu_adresse(objet[1], int(objet[2])))

    def inventaire(self):
        for objet in self.liste_objet:
            if objet.nom == self.choix:
                objet.quantite -= self.qtt

    def achat (self):
        self.choix.achat()

#Fais attention de ne pas hard code des sélection. rends ton code dynamique.
    # def pochettes(self):
    #     if self.choix == "Uno":
    #         for objet in self.liste_objet:
    #             if objet.nom == "Uno":
    #                 # objet.couleur = input("Choisissez la couleur de votre pochette : ")
    #                 objet.achat()
    #                 print(objet.object_pochette)
    #     elif self.choix == "Solitaire":
    #         for objet in self.liste_objet:
    #             if objet.nom == "Solitaire":
    #                 # objet.couleur = input("Choisissez la couleur de votre pochette : ")
    #                 objet.achat()
    #                 print(objet.object_pochette)
    # def doc(self):
    #     if self.choix == "Malefices":
    #         for objet in self.liste_objet:
    #             if objet.nom == "Malefices":
    #                 print("Documentation")
    #     elif self.choix == "Kuro":
    #         for objet in self.liste_objet:
    #             if objet.nom == "Kuro":
    #                 print("Documentation")

    # def tournoi(self):
    #     if self.choix == "Elvenar":
    #         for objet in self.liste_objet:
    #             if objet.nom == "Elvenar":
    #                 objet.couleur = input("Choisissez la couleur de votre pochette : ")
    #     elif self.choix == "Grepolis":
    #         for objet in self.liste_objet:
    #             if objet.nom == "Grepolis":
    #                 objet.couleur = input("Choisissez la couleur de votre pochette : ")

    def afficher(self):
        for objet in self.liste_objet:
            if objet.quantite > 0:
                print(objet)

    def commande(self):
        self.choix = input("\nChoisir un jeu : ").capitalize()
        self.qtt = int(input("Combien de ce jeu voulez vous ? "))

    def menu(self):
        condition = True
        while condition:
            print("\n\t--Binvenue dans note magasin de jeux--")
            choix = input("\n(1). Acheter un jeu "
                        "\n(2). Voir l'inventaire "
                        "\n(3). Quiter"
                        "\nVotre choix : ")

            if choix == "1":
                print("\nVoici les jeux disponibles")
                self.afficher()
                self.commande()
                self.inventaire()
                self.achat()
            elif choix == "2":
                self.afficher()
            elif choix == "3":
                condition = False

class Jeu:
 
    def __str__(self) -> str:
        return f"Jeu : {self.nom} \tQuantité en stock disponible {self.quantite} "

#Surcharge la même méthode dans toutes tes classes pour éviter d'avoir à trouver son type.
class Jeu_carte(Jeu):
    def __init__(self,nom, quantite):
        super(). __init__()
        self.type = "Jeux de cartes"
        self.couleur = ""
        self.object_pochette = None #Pochette(self.couleur)
        self.nom = nom
        self.quantite = quantite

    def achat(self):
        #choisir user color ici
        couleur = input("Choisissez la couleur de votre pochette : ")
        # self.object_pochette = Magasin.choisir_pochette(couleur)
        self.object_pochette = Pochette(couleur)

    def afficher(self):
        print(self.object_pochette)


class Uno(Jeu_carte):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite
        

class Solitaire(Jeu_carte):
    def __init__(self, quantite):
        super().__init__(nom, quantite)
        self.quantite = quantite


class Jeu_strategie(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__()
        self.type = "Jeux de strategie"
        self.nom = nom
        self.quantite = quantite
        self.objet_tournoi = ""

    def achat(self):
        nom = input("Entrez votre nom : ")
        prenom = input("Entrez votre prenom : ")
        courriel= input("Choisissez la couleur de votre pochette : ")
        # self.object_pochette = Magasin.choisir_pochette(couleur)
        self.objet_tournoi= Tournoi(nom, prenom, courriel)

class Elvenar(Jeu_strategie):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite

class Grepolis(Jeu_strategie):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite

class Jeur_role(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__()
        self.documentation = ""
        self.type = "jeu de rôle"
        self.nom = nom
        self.quantite = quantite

    def achat(self):
        print("Voici la documentation de votre jeu : ")

class Malefices(Jeur_role):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite

class Kuro (Jeur_role):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite
        

class Jeu_assemblage(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__()
        self.type = "jeu d'assemblage"
        self.nom = nom
        self.quantite = quantite

    def achat(self):
        print(" Voila votre jeu ")

class Casse_tete(Jeu_assemblage):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite

class Rubiks_cube(Jeu_assemblage):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite

class Jeu_adresse(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__()
        self.type = "jeu d'adresse'"
        self.nom = nom
        self.quantite = quantite

    def achat(self):
        print(" Voila votre jeu ")

class Monopolie(Jeu_adresse):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite

class Mahjong(Jeu_adresse):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite

class Tournoi:
    def __init__(self, nom, prenom, courriel):
        self.nom = nom
        self.prenom = prenom
        self.courriel = courriel
        self.date = ""

    def __str__(self) -> str:
        return f"Mr {self.nom} vous ete inscrit dans le tournoi regionel qui aura lieu le {self.date}"

class Pochette:
    def __init__(self, couleur):
        self.couleur = couleur

    def __str__(self):
        return (f"Voici votre pochette plastifiante {self.couleur}")


m = Magasin()
m.menu()






