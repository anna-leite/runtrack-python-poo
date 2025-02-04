class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.en_marche = False
        self.__reservoir = 50

    # assesseurs
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.en_marche
    
    def __verifier_plein(self):
        return self.__reservoir
    
    # mutateurs
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage


    def demarrer(self):
        if self.__verifier_plein() > 5 :
            self.en_marche = True

    def arreter(self):
        self.en_marche = False


# instance
voiture1 = Voiture("Alpha Romer", "Gulietta", 1969, 60000)
voiture1.demarrer()

print(f"{voiture1.en_marche}")






        