class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2


#instancier un objet
objet = Operation(12, 3)

# impression d'un attribut de l'objet
print(f"Le nombre1 est {objet.nombre1}")
print(f"Le nombre1 est {objet.nombre2}")