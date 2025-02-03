class Operation():
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        return self.nombre1 + self.nombre2
    
    def __str__(self):
        return f"{self.nombre1}, {self.nombre2}"


#instancie un objet
objet = Operation(12, 3)

# appelle une méthode sur un objet instancié
resultat = objet.addition()

print(resultat)
        