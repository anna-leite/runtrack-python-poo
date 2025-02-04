class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

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





    

# instance

livre1 = Livre("Sur la route", "Jack Kerouac", 400)

print(f"{livre1.get_titre()}, {livre1.get_auteur()}, {livre1.get_nb_pages()}")

livre1.set_titre("Du côté de Guermante")
livre1.set_auteur("Marcel Proust")
livre1.set_nb_pages("ert")

print(f"{livre1.get_titre()}, {livre1.get_auteur()}, {livre1.get_nb_pages()}")


