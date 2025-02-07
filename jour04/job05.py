from math import *

class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, rayon):
        super().__init__()
        self.__rayon = rayon

    def aire(self):
        return 2* pi *self.__rayon
    
class Rectancle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.__largeur = largeur
        self.__hauteur = hauteur

    def aire(self):
        return self.__largeur * self.__hauteur



rectangle1 = Rectancle(4, 7)
print(rectangle1.aire())

cercle1 = Cercle(5)
print(cercle1.aire())