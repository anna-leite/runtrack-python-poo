class Tache:
    def __init__(self, titre, description):
        self.__titre = titre 
        self.__description = description
        self.__statut = "à faire"

    def get_titre(self):
        return self.__titre
    
    def get_description(self):
        return self.__description

    def get_statut(self):
        return self.__statut
    
    def set_statut(self):
        self.__statut = "terminé"



class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def get_liste(self):
        return self.__taches

    def ajouterTache(self, instance_tache):
        self.__taches.append(instance_tache)

    def supprimerTache(self, instance_tache):
        self.__taches.reverse()
        for i in range(0, len(self.__taches)): 
            if instance_tache.get_titre() == self.__taches[i].get_titre():
                self.__taches.pop(i)

    def marquerCommeFinie(self, instance_tache):
        instance_tache.set_statut()


    def afficherListe(self):
        for i in range(0, len(self.__taches)):
            print(f"\n\nTache : {self.__taches[i].get_titre()},\nDescription : {self.__taches[i].get_description()},\nStatut :{self.__taches[i].get_statut()}")

    def filtrerListe(self, statut):
        for i in range(0, len(self.__taches)):
            if statut == self.__taches[i].get_statut():
                print(f"\n\nTache : {self.__taches[i].get_titre()},\nDescription : {self.__taches[i].get_description()}")





tache1 = Tache("courses", "pomme, patate, jambon")
tache2 = Tache("Coiffeur", "chez Mavro")
tache3 = Tache("CV", "Finir CV")
tache4 = Tache("RDV doc", "mardi 5 à 15h")

liste = ListeDeTaches()
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)
liste.ajouterTache(tache4)

liste.marquerCommeFinie(tache1)
liste.marquerCommeFinie(tache3)

liste.afficherListe()


# liste.supprimerTache(tache1)
liste.filtrerListe("terminé")

