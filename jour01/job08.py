from math import pi

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        
    def changerRayon(self, rayon):
        self.rayon = rayon

    def diametre(self):
        return self.rayon * 2  

    def circonference(self):
        return self.rayon * 2 * pi
    
    def aire(self):
        return pi * self.rayon**2

    def afficherInfos(self):
        print(f"Le rayon du cercle est : {self.rayon},\nson diamètre est : {self.diametre()},\nsa circonférence est : {self.circonference()},\net son aire est : {self.aire()}\n")

    
cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()

cercle2.afficherInfos()

