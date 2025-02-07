class Personne:
    def __init__(self):
        self.__age = 14

    def afficherAge(self):
        return self.__age

    def bonjour(self):
        print(f"Hello")

    def modifierAge(self, age):
        if isinstance(age, int) == True and age > 0:
            self.__age = age
        else : print("Saisie incorrecte, l'age doit être entré sous forme d'entier positif.")


class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {Personne.afficherAge(self)} ans")

class Professeur(Personne):
    def __init__(self, matiere_enseignee):
        super().__init__()
        self.__matiereEnseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours commence")


eleve1 = Eleve()

eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
eleve1.afficherAge()

professeur1 = Professeur("math")
professeur1.modifierAge(40)
print(professeur1.afficherAge())
professeur1.bonjour()
professeur1.enseigner()