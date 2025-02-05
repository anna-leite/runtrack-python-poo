class CompteBancaire:
    def __init__(self, num_compte, nom, prenom ):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = 0
        self.__decouvert = False
    
    def get_num_compte(self):
        return self.__num_compte

    def afficher_solde(self):
         print(f"Solde : {self.__solde}")
    
    def afficher(self):
        print(f"Numéro de compte : {self.__num_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")

    def versement(self, versement):
        self.__solde += versement


    def retrait(self, retrait):
        if self.__decouvert == True :
            self.__solde -= retrait
        elif self.__decouvert == False and self.__solde > retrait:
            self.__solde -= retrait
        else :
            print("Retrait impossible, votre solde est trop bas. Vous n'avez pas d'autorisation de découvert.")

    def autorisation_decouvert(self):
        self.__decouvert = True

    def agios(self):
        self.__solde -= (self.__solde * (5/100))

    def virement(self, ref, instance_compte, montant):
        if self.__decouvert == True :
            self.__solde -= montant
            instance_compte.versement(montant)
            print(f"Virement numero {ref}, de {montant} euros sur le compte numéro {instance_compte.get_num_compte()} est réussi!")
        elif self.__decouvert == False and self.__solde > montant:
            self.__solde -= montant
            instance_compte.versement(montant)
            print(f"Virement numero {ref}, de {montant} euros sur le compte numéro {instance_compte.get_num_compte()} est réussi!")
        else :
            print(f"Echec virement numero {ref}. Votre solde est trop bas. Vous n'avez pas d'autorisation de découvert.")   





compte1 = CompteBancaire(145, "LEITE", "Anna")
compte2 = CompteBancaire(146, "DOE", "John")

compte1.afficher()
compte1.versement(30)
compte1.afficher_solde()
# compte1.afficher_solde()
compte1.autorisation_decouvert()

# compte1.retrait(200)
# compte1.afficher_solde()

# compte1.agios()
# compte1.afficher_solde()

compte2.autorisation_decouvert()
compte2.retrait(40)
compte2.afficher()
compte2.afficher_solde()

compte1.virement(23, compte2, 40)

compte1.afficher_solde()
compte2.afficher_solde()


