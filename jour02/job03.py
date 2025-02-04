class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    # assesseurs
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    # mutateurs
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) == True and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else :
            print("La saisie est incorrect. Essayez a nouveau, attention la saisie doit être un entier positif.")

    # assesseur (?)
    def verification(self):
        return self.__disponible

    # mutateur (?)
    def emprunter(self):
        if self.verification() == True :
            self.__disponible = False
        else :
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if self.verification() == False :
            self.__disponible = True




