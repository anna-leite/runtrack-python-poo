class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0
    
class Rectancle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.__largeur = largeur
        self.__hauteur = hauteur

    def aire(self):
        return self.__largeur * self.__hauteur
    

rectangle1 = Rectancle(4, 7)
print(rectangle1.aire())
