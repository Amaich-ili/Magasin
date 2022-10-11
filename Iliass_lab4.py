"""
Iliass Amaich
Laboratoire 4
Session été 2022

"""
from random import randint

class Magasin:
    qtt_vendu = int
    def __init__(self):
        self.liste_objet = []
        self.choix = None
        self.dict_jeu = {
                        "Uno": Uno, "Solitaire" : Solitaire, "Elvenar": Elvenar, 
                        "Grepolis": Grepolis, "Malefices":Malefices, "Kuro": Kuro,
                        "Casse_tete": Casse_tete, "Rubik's_cube": Rubiks_cube,
                        "Monopolie": Monopolie, "Mahjong": Mahjong
                        }

        with open("fichier.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                jeu = line.split()
                self.liste_objet.append(self.dict_jeu[jeu[0]](jeu[0],int(jeu[1])))

    def stock(self):
        for objet in self.liste_objet:
            if objet.nom == self.choix:
                objet.quantite -= Magasin.qtt_vendu

    def achat (self):
        self.choix = input("\nVeuillez écrire le nom de jeu : ").capitalize()
        Magasin.qtt_vendu = int(input("\nCombien de ce jeu voulez vous ?  "))
        with open("fichier.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                jeu = line.split()
                return self.dict_jeu[self.choix](jeu[0],int(jeu[1])).achat()

    def afficher(self):
        for objet in self.liste_objet:
            if objet.quantite > 0:
                print(objet)

    def inventaire(self):
        for objet in self.liste_objet:
            print(f"{objet} Quantite en stock : {objet.quantite}")

    def menu(self):
        condition = True
        while condition:
            print("\n\t--Binvenue dans note magasin de jeux--")
            choix = input("\n(1). Acheter un jeu "
                          "\n(2). Voir l'inventaire "
                          "\n(3). Quiter"
                          "\nMerci de choisir une option (1-3): ")

            if choix == "1":
                print("\nVoici les jeux disponibles\n")
                self.afficher()
                self.achat()
                self.stock()
            elif choix == "2":
                self.inventaire()
            elif choix == "3":
                condition = False

class Jeu:
    def __str__(self):
        return f"Jeu : {self.nom} "

class Jeu_carte(Jeu):
    def __init__(self):
        super(). __init__()
        self.pochette = None

    def achat(self):
        for i in range(Magasin.qtt_vendu):
            couleur = input(f"Merci de Choisir la couleur de votre pochette numero {i+1}: ")
            self.pochette = Pochette(couleur)
            print(f"{self.pochette}pour votre jeu {self.nom}")

class Uno(Jeu_carte):
    def __init__(self, nom ,quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite
        
class Solitaire(Jeu_carte):
    def __init__(self, nom, quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite

class Jeu_strategie(Jeu):
    def __init__(self):
        super(). __init__()
        self.tournoi = None
        self.liste_tournoi= []

    def achat(self):
        participe = input("Voulez vous participer à un Tournoi (oui/non): ")
        if participe == "oui":
            self.tournoi = Tournoi(self.nom)
            self.liste_tournoi.append(Tournoi(self.tournoi))
            nom = input("Entrez votre nom : ")
            courriel= input("Entrer votre courrriel : ")
            self.tournoi.liste_participants.append(participant(nom, courriel))
            print(self.tournoi)         
        else:
            pass

    def afficher_tournoi(self):
        print("Voici la liste de participants: ")
        for participant in self.tournoi.liste_participant:
            print(participant)

class Elvenar(Jeu_strategie):
    def __init__(self, nom, quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite
        
class Grepolis(Jeu_strategie):
    def __init__(self, nom, quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite

class Tournoi:
    def __init__(self, nom):
        self.nom = nom
        self.date = f"2022-{randint(11,12)}-{randint(1,2)}"
        self.liste_participants = []

    def __str__(self):
        return f"\n Félicitation vous êtes inscrit au tournoi regionel qui aura lieu le {self.date}"

class participant:
    def __init__(self, nom, courriel):
        self.nom = nom
        self.courriel = courriel

    def __str__(self):
       return f"Le nom de participant : {self.nom} - Courriel : {self.courriel}"
        
class Jeur_role(Jeu):
    def __init__(self):
        super(). __init__()  

class Malefices(Jeur_role):
    def __init__(self, nom, quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite
    
    def achat(self):
        print("Voici la documentation de votre jeu : "
        "\nMaléfices est un jeu de rôle occulte et mystérieux se déroulant en "
        "France à la Belle Époque (1870-1914). Durant cette période charnière" 
        "entre les XIXe et XXe siècles, les superstitions sont encore vives,"
        "surtout dans les campagnes où l’on ne plaisante pas avec le Malin.") 
        
class Kuro (Jeur_role):
    def __init__(self, nom, quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite

    def achat(self):
        print("Voici la documentation de votre jeu : "
        "\nKuro est un jeu de rôle édité par Le Septième Cercle" 
        "et paru en 2007. Il tourne autour de 3 thèmes majeurs :" 
        "le Japon, la technologie et l'horreur.Les personnages-joueurs "
        "sont des habitants du Japon – japonais ou étrangers – désormais "
        "prisonniers du blocus. Ils sont, comme tous les autres, confrontés "
        "à des phénomènes paranormaux, comme si les légendes médiévales prenaient vie. ")
        
class Jeu_assemblage(Jeu):
    def __init__(self):
        super(). __init__()
     
    def achat(self):
        print(" \n--Voici votre jeu , Bonne journee--")

class Casse_tete(Jeu_assemblage):
    def __init__(self, nom, quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite

class Rubiks_cube(Jeu_assemblage):
    def __init__(self, nom, quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite

class Jeu_adresse(Jeu):
    def __init__(self):
        super(). __init__()

    def achat(self):
        print(" \n--Voici votre jeu , Bonne journee--")

class Monopolie(Jeu_adresse):
    def __init__(self, nom, quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite

class Mahjong(Jeu_adresse):
    def __init__(self, nom, quantite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite

class Pochette:
    def __init__(self, couleur):
        self.couleur = couleur

    def __str__(self):
        return (f"\nVoici votre pochette plastifiante {self.couleur} ")

class participant:
    def __init__(self, nom, courriel):
        self.nom = nom
        self.courriel = courriel

    def __str__(self) -> str:
       return f"Le nom de participant : {self.nom} - Courriel : {self.courriel}"



m = Magasin()
m.menu()
