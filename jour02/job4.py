class Student:
    def __init__(self, lastname, firstname, student_number):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__student_number = student_number
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, grade):
        if isinstance(grade, (int, float)) == True and grade > 0:
            self.__credits += grade
            self.__level = self.__student_eval()
        else :
            print("Incorrect input.")

    # def get_lastname(self):
    #     return self.__lastname
    
    # def get_firstname(self):
    #     return self.__firstname
    
    def get_level(self):
        return self.__level
    
    # def get_credits(self):
    #     return self.__credits
    
    # def print_credits(self):
    #     print(f"Le nombre de credits de {self.__firstname} {self.__lastname} est de {self.__credits} points")

    def __student_eval(self):
        if self.__credits >= 90 :
            self.__level = "Excellent"
        elif 90 > self.__credits >= 80 :
            self.__level = "Très bien"
        elif 80 > self.__credits >= 70 :
            self.__level = "Bien"
        elif 70 > self.__credits >= 60 :
            self.__level = "Passable"
        elif self.__credits < 60 :
            self.__level = "Insuffisant"
        return self.__level
    
    def student_info(self):
        print(f"Nom = {self.__firstname}")
        print(f"Prénom = {self.__lastname}")
        print(f"id = {self.__student_number}")
        print(f"Niveau = {self.__level}")



# instance
student1 = Student("Doe", "John", 145)

student1.add_credits(50)
student1.add_credits(15)

print(f"{student1.get_level()}")


# student1.print_credits()

student1.student_info()

