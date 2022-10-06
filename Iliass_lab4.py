"""
Iliass Amaich
Laboratoire 4
Session été 2022

"""

class Magasin:
    qtt_vendu = int
    def __init__(self):
        self.liste_objet = []
        self.choix = ""
        # self.qtt = int
        self.dict_jeu = {
                        "Uno": Uno, "Solitaire" : Solitaire, "Elvenar": Elvenar, 
                        "Grepolis": Grepolis, "Malefices":Malefices, "Kuro": Kuro,
                        "Casse_tete": Casse_tete, "Rubik's_cube": Rubiks_cube,
                        "Monopolie": Monopolie, "Mahjong": Mahjong
                        }
        # self.dict_type_jeu: {"Jeu_carte": Jeu_carte, "Jeu_strategie"

        # }
        
        with open("fichier.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                objet = line.split()
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
                objet.quantite -= Magasin.qtt_vendu
                print(f"{objet} Quantite en stock : {objet.quantite}")

    def achat (self):
        with open("fichier.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                jeu = line.split()
                return self.dict_jeu[self.choix](jeu[1],int(jeu[2])).achat()

    def afficher(self):
        for objet in self.liste_objet:
            if objet.quantite > 0:
                print(objet)

    def commande(self):
        self.choix = input("\nChoisir un jeu : ").capitalize()
        Magasin.qtt_vendu = int(input("Combien de ce jeu voulez vous ? "))

    def menu(self):
        condition = True
        while condition:
            print("\n\t--Binvenue dans note magasin de jeux--")
            choix = input("\n(1). Acheter un jeu "
                          "\n(2). Voir l'inventaire "
                          "\n(3). Quiter"
                          "\nMerci de choisir une option (1 - 3): ")

            if choix == "1":
                print("\nVoici les jeux disponibles")
                self.afficher()
                self.commande()
                self.achat()
            elif choix == "2":
                self.inventaire()
            elif choix == "3":
                condition = False

class Jeu:
    def __str__(self) -> str:
        return f"Jeu : {self.nom} "

class Jeu_carte(Jeu):
    def __init__(self,nom, quantite):
        super(). __init__()
        self.type = "Jeux de cartes"
        self.couleur = ""
        self.object_pochette = None
        self.nom = nom
        self.quantite = quantite

    def achat(self):
        for i in range(Magasin.qtt_vendu):
            couleur = input(f"Merci de Choisir la couleur de votre pochette numero {i+1}: ")
            self.object_pochette = Pochette(couleur)
            print(f"{self.object_pochette}pour votre jeu {self.nom}")

class Uno(Jeu_carte):
    def __init__(self, nom ,quantite):
        super().__init__(nom, quantite)
        self.nom = nom
        self.quantite = quantite
        
class Solitaire(Jeu_carte):
    def __init__(self, nom, quantite):
        super().__init__(nom, quantite)
        self.nom = nom
        self.quantite = quantite


class Jeu_strategie(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__()
        self.type = "Jeux de strategie"
        self.nom = nom
        self.quantite = quantite
        self.objet_tournoi = "tournoi"

    # def achat(self):
    #     participe = input("Voulez vous participer à un Tournoi (oui/non): ")
    #     # tournoi
    #     # for tournoi in tournois:
    #     #     print(tournoi)
    #     if participe == "oui":
    #         if 
    #     nom = input("Entrez votre nom : ")
    #     prenom = input("Entrez votre prenom : ")
    #     courriel= input("Entrer votre courrriel : ")
    #     # self.object_pochette = Magasin.choisir_pochette(couleur)
    #     self.objet_tournoi= Tournoi(nom, courriel)

class Elvenar(Jeu_strategie):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite
        self.liste_tournoi= []
        self.liste_participant= []
    
    def achat(self):
        participe = input("Voulez vous participer à un Tournoi (oui/non): ")
        if participe == "oui":
            nom = input("Entrez votre nom : ")
            courriel= input("Entrer votre courrriel : ")
            self.liste_participant.append(participant(nom, courriel))
            self.liste_tournoi.append(Tournoi())
        else:
            pass
        
        
        

class Grepolis(Jeu_strategie):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite
        self.liste_tournoi= []
        self.liste_participant = []
    
    def achat(self):
        participe = input("Voulez vous participer à un Tournoi (oui/non): ")
        if participe == "oui":
            nom = input("Entrez votre nom : ")
            courriel= input("Entrer votre courrriel : ")
            self.liste_participant.append(participant(nom, courriel))
            self.liste_tournoi.append(Tournoi())
        else:
            pass
        
class Jeur_role(Jeu):
    def __init__(self, nom, quantite):
        super(). __init__()
        self.documentation = ""
        self.type = "jeu de rôle"
        self.nom = nom
        self.quantite = quantite

class Malefices(Jeur_role):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite
    
    def achat(self):
        print("Voici la documentation de votre jeu : "
        "\nMaléfices est un jeu de rôle occulte et mystérieux se déroulant en "
        "France à la Belle Époque (1870-1914). Durant cette période charnière" 
        "entre les XIXe et XXe siècles, les superstitions sont encore vives,"
        "surtout dans les campagnes où l’on ne plaisante pas avec le Malin.") 
        
class Kuro (Jeur_role):
    def __init__(self, quantite):
        super().__init__()
        self.quantite = quantite

    def achat(self):
        print("Voici la documentation de votre jeu : "
        "\nKuro est un jeu de rôle édité par Le Septième Cercle" 
        "et paru en 2007. Il tourne autour de 3 thèmes majeurs :" 
        "le Japon, la technologie et l'horreur.")
        

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
    # dict_tournois = {"16/10/22": "Durandal en guerre 2",
    #                 "28/10/22":"BRETZWARS 4",
    #                 "16/11/22":"La Pitounerie",
    #                 "20/10/22":"Majestik conquest"}
    def __init__(self):
        # self.nom = nom
        # self.prenom = prenom
        # self.courriel = courriel
        # self.date = ""

        print("voici les Tournois à venir :")
        for key, values in Tournoi.dict_tournois.items():
            print(f"{key} - {values}" )
        nom = input("Entrez votre nom : ")
        prenom = input("Entrez votre prenom : ")
        courriel= input("Entrer votre courrriel : ")
        # self.object_pochette = Magasin.choisir_pochette(couleur)
        self.objet_tournoi= Tournoi(nom, prenom, courriel)

    def __str__(self) -> str:
        return f"Mr {self.nom} vous ete inscrit dans le tournoi regionel qui aura lieu le {self.date}"

class Pochette:
    def __init__(self, couleur):
        self.couleur = couleur

    def __str__(self):
        return (f"Voici votre pochette plastifiante {self.couleur} ")

class participant:
    def __init__(self, nom, courriel):
        self.nom = nom
        self.courriel = courriel

    def __str__(self) -> str:
       return f"Le nom de participant : {self.nom} - Courriel : {self.couriel}"

m = Magasin()
m.menu()






