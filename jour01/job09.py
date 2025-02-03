class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return (self.prixHT * (self.TVA/100)) + self.prixHT
    
    def afficher(self):
        return f"Nom du produit : {self.nom}\nPrix HT : {self.prixHT} euros\nTVA : {self.TVA}%\nPrix TTC : {self.calculerPrixTTC()} euros"
    
    def nouveauNom(self):
        self.nom = input("Nouveau nom :")

    def nouveauPrix(self):
        self.prixHT = int(input("Nouveau prix HT :"))

    def afficherNom(self):
        return f"Nom du produit : {self.nom}"
    
    def afficherPrixHT(self):
        return f"Prix HT : {self.prixHT} euros"
    
    def afficherTVA(self):
        return f"TVA : {self.TVA}%"
    
    def afficherPrixTTC(self):
        return f"Prix TTC : {self.calculerPrixTTC()} euros"






produit1 = Produit("Bière", 6, 20)
produit2 = Produit("Mousse au chocolat", 5, 12)
produit3 = Produit("Café", 1, 5)


print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

produit1.nouveauNom()
produit1.nouveauPrix()

print(produit1.afficherPrixTTC())
print(produit1.afficher())