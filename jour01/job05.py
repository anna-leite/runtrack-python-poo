class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées des points sont : {self.x}, {self.y}") 

    def afficherX(self):
        print(f"L'abscisse du point est : {self.x}")

    def afficherY(self):
        print(f"L'ordonnée du point est : {self.y}")

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y



