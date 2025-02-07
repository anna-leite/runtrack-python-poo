class Carte:
    def __init__(self, couleur, valeur):
        self.__couleur = couleur
        self.__valeur = valeur


    def getAttributs(self):
        return (self.__couleur, self.__valeur) # retourne un tuple
    
    def afficherCarte(self):
        return f"{self.__valeur} de {self.__couleur}"
    

class JeuDeCarte(Carte):
    def __init__(self):
        super().__init__()
        self.__nombre_cartes = 52
        self.__paquet_cartes = []

    def creerPaquet(self):
        for i in range(1, 14):
            if 



    def distribuerUneCarte(self):
        pass

    def melangerJeu(self):
        pass




carte1 = Carte(10, "coeur")
print(type(carte1.getAttributs()))
    
# trèfle, pique, coeur, carreau

