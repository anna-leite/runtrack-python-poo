class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = []
        self.__statut_commande = "en cours"

    # assesseurs 
    def get_numero_commande(self):
        return self.__numero_commande
    
    def get_plats_commandes(self):
        return self.__plats_commandes
    
    def get_statut_commande(self):
        return self.__statut_commande
    

    # mutateurs
    def clore_commande(self): # nécessaire pour lancer le calcul de la note
        self.__statut_commande = "terminée"

    def commande_annulee(self): 
        self.__statut_commande = "annulée"

    def ajouter_plat(self):
        # gérer les erreurs input
        nom_plat = input("nom du plat :",)
        prix_plat = float(input("prix du plat :",))
        plat_ajoute = {"plat": nom_plat, "prix" : prix_plat, "statut": True}
        self.__plats_commandes.append(plat_ajoute)

    def annuler_plat(self):
        """change la valeur de statut dans le dictionnaire du plat, 
        il ne sera pas pris en compte lors du calcul de la note"""
        plat_annulé = input("plat annulé :",)
        for i in range(0, len(self.__plats_commandes)) :
            if plat_annulé == self.__plats_commandes[i]['plat']:
                self.__plats_commandes[i]['statut'] = False

    def __total_commande(self):
        if self.__statut_commande == 'terminée' : # possible uniquement si la commande est close
            total = 0
            for i in range(0, len(self.__plats_commandes)):
                if self.__plats_commandes[i]['statut'] == True :
                    total += self.__plats_commandes[i]['prix']

        return total
    
    def __calcul_TVA(self) :
        return self.__total_commande()* (10/100)
    
    def afficher_total_commande(self):
        print("NOTE ///////")
        print(f"Numéro de commande : {self.__numero_commande}")
        for i in range (0, len(self.__plats_commandes)):
            if self.__plats_commandes[i]['statut'] == True:
                print(f"{self.__plats_commandes[i]['plat']} : {self.__plats_commandes[i]['prix']} euros")
            elif self.__plats_commandes[i]['statut'] == False:
                print(f"{self.__plats_commandes[i]['plat']} : annulé")
        print(f"Le total de la commande est : {self.__total_commande()} euros")
        print(f"Montant de la TVA : {self.__calcul_TVA()} euros")



# instance 
commande1 = Commande(1)

commande1.ajouter_plat()
commande1.ajouter_plat()
commande1.ajouter_plat()
commande1.annuler_plat()
commande1.clore_commande()

print(f"{commande1.get_plats_commandes()}")

commande1.afficher_total_commande()




 