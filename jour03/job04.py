class Joueur:
    def __init__(self, nom, numero, position, buts_marques, passes_decisives, cartons_jaunes, cartons_rouges):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts_marques = buts_marques
        self.__passes_decisives = passes_decisives
        self.__cartons_jaunes = cartons_jaunes
        self.__cartons_rouges = cartons_rouges

    def marquerUnBut(self):
        self.__buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.__passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistique de {self.__nom} :")
        print(f"Numéro : {self.__numero}, Position : {self.__position}")
        print(f"Buts marqués : {self.__buts_marques}")
        print(f"Passes décisives : {self.__passes_decisives}")
        print(f"Cartons jaunes : {self.__cartons_jaunes}")
        print(f"Cartons rouges : {self.__cartons_rouges}")

        
        

class EquipeFoot:
    def __init__(self, nom_equipe):
        self.__nom_equipe = nom_equipe
        self.__liste_joueurs = []

    def ajouterJoueur(self, instance_joueur):
        self.__liste_joueurs.append(instance_joueur)

    def AfficherStatistiquesJoueurs(self):

    def mettreAJourStati


