class Ville:
    def __init__(self, nom_ville, nb_habitant):
        self.__nom_ville = nom_ville
        self.__nb_habitant = nb_habitant

    # assesseur
    def get_nom_ville(self):
        return self.__nom_ville
    
    def get_nb_habitant(self):
        return self.__nb_habitant
    
    # mutateur
    def set_nb_habitant(self):
        self.__nb_habitant += 1
    
    def affiche_info(self):
        print(f"Population de la ville de {self.__nom_ville} : {self.__nb_habitant} habitants")

    def affiche_actualisation_population(self):
        print(f"Mise à jour de la population de la ville de {self.__nom_ville} : {self.__nb_habitant} habitants")

class Personne:
    def __init__(self, nom, age, instance_ville):
        self.__nom = nom
        self.__age = age
        self.__ville = instance_ville

    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville

    def ajouter_population(self):
        self.__ville.set_nb_habitant()

    def affiche_situation(self):
        print(f"{self.__nom}, {self.__age} ans, habitant à {self.__ville.get_nom_ville()}")



ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)

ville1.affiche_info()
ville2.affiche_info()


personne1 = Personne("Jonh", 45, ville1)
personne2 = Personne("Myrtille", 4, ville1)
personne3 = Personne("Chloé", 18, ville2)

# personne1.affiche_situation()
# personne2.affiche_situation()
# personne3.affiche_situation()

personne1.ajouter_population()
personne2.ajouter_population()
personne3.ajouter_population()

ville1.affiche_actualisation_population()
ville2.affiche_actualisation_population()



