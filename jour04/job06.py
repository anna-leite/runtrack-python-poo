class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix

    def informationsVehicule(self):
        # return self.__marque, self.__modele, self.__annee, self.__prix
        print(f"Marque = {self.__marque}")
        print(f"Modèle = {self.__modele}")
        print(f"Année = {self.__annee}")
        print(f"Prix = {self.__prix} euros")

    def demarrer(self):
        print("Attention, je roule")
    

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.__portes = 4

    def informationsVehicule(self):
        # return super().informationsVehicule(), self.__portes
        # return Vehicule.informationsVehicule(self), self.__portes 
        super().informationsVehicule()
        print(f"Nombre de portes = {self.__portes}")

    def demarrer(self):
        super().demarrer()
        print("Je consomme un max")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.__roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues = {self.__roues}")

    def demarrer(self):
        super().demarrer()
        print("Sans casque")



# vehicule1 = Vehicule("Renault", "Megane", 2000, 8000)
# print(type(vehicule1.informationsVehicule())) => tuple !!!
# print(vehicule1.informationsVehicule()[1])

voiture1 = Voiture("Mercedes", "Classe A", 2020, 18500)

# essai affichage terminal avec index du tuple retourné par methode informationsVehicule()
# un peu trop lourd 
# print(f"Marque = {voiture1.informationsVehicule()[0][0]}")
# print(f"Modèle = {voiture1.informationsVehicule()[0][1]}")
# print(f"Année = {voiture1.informationsVehicule()[0][2]}")
# print(f"Prix = {voiture1.informationsVehicule()[0][3]} euros")
# print(f"Nombre de portes = {voiture1.informationsVehicule()[1]} portes")

voiture1.informationsVehicule()
voiture1.demarrer()

moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto1.informationsVehicule()
moto1.demarrer()
