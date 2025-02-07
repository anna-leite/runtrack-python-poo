class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # assesseurs
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    # mutateurs
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    def perimetre(self):
        return 2 * self.__longueur + 2 * self.__largeur
    
    def surface(self):
        return self.__longueur * self.__largeur
        

class Parallelepipede(Rectangle):
    def __init__(self,longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return Rectangle.surface(self) * self.__hauteur
    

rectangle1 = Rectangle(3, 5)
parallelepipede1 = Parallelepipede(3, 5, 5)
print(rectangle1.perimetre())
print(rectangle1.surface())
print(parallelepipede1.volume())

