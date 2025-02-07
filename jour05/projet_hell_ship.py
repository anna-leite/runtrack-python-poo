class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material


    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return (f"la partie {self.name} est en {self.material}")


class Ship:
    def __init__(self, name_ship):
        self.name_ship = name_ship
        self.__parts = {}


    def add_part(self, instance):
        self.__parts[instance.name] = instance # pour la cle 'nom de la partie' stock (partie et matière)


    def display_state(self):
        print(f"Etat  du navire {self.name_ship} :")
        for part in self.__parts.values():
            print(part) # appelle la méthode __str__


    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
        else :
            print(f"La pièce {part_name} n'existe pas dans le navire.")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
        else :
            print(f"La pièce {part_name} n'existe pas dans le navire.")


class RacingShip(Ship):
    def __init__(self, name_ship, max_speed):
        super().__init__(name_ship)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"La vitesse maximale du bateau {self.name_ship} est  de {self.max_speed} noeuds.")


def display_menu():
    print("\nMenu interactif:")
    print("1. Ajouter une pièce")
    print("2. Remplacer une pièce")
    print("3. Modifier le matériau d'une pièce")
    print("4. Afficher l'état du navire")
    print("5. Afficher la vitesse maximale (pour RacingShip)")
    print("6. Afficher l'historique des modifications")
    print("7. Quitter")

def main():
    # Création de quelques pièces
    part1 = Part("Mât", "Bois")
    part2 = Part("Coque", "Acier")
    part3 = Part("Voile", "Tissu")

    # Création d'un navire de course
    ship = RacingShip("Navire de Course", 30)

    while True:
        display_menu()
        choice = input("Choisissez une option: ")

        if choice == "1":
            part_name = input("Nom de la pièce à ajouter: ")
            part_material = input("Matériau de la pièce: ")
            new_part = Part(part_name, part_material)
            ship.add_part(new_part)
        elif choice == "2":
            part_name = input("Nom de la pièce à remplacer: ")
            part_material = input("Nouveau matériau de la pièce: ")
            new_part = Part(part_name, part_material)
            ship.replace_part(part_name, new_part)
        elif choice == "3":
            part_name = input("Nom de la pièce à modifier: ")
            new_material = input("Nouveau matériau: ")
            ship.change_part(part_name, new_material)
        elif choice == "4":
            ship.display_state()
        elif choice == "5":
            ship.display_speed()
        elif choice == "6":
            ship.display_history()
        elif choice == "7":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()



                    

        



            
    