class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # accesseur
    def get_longueur(self):
        return self.__longueur 
    
    # mutateur
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    # accesseur
    def get_largeur(self):
        return self.__largeur

    # mutateur
    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

        
# instance
rectangle1 = Rectangle(10, 5)

print(f"{rectangle1.get_longueur()}, {rectangle1.get_largeur()}")

rectangle1.set_longueur(12)
rectangle1.set_largeur(7)

print(f"{rectangle1.get_longueur()}, {rectangle1.get_largeur()}")
