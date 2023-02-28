type_of_animal = input("Введите вид персонажа: ")
name = input("Введите имя персонажа: ")
sex = input("Введите пол персонажа: ")
color = input("Введите цвет персонажа: ")

class Animal:
    def __init__(self, name, type_of_animal, sex, color):
        self.name = name
        self.type_of_animal = type_of_animal
        self.age = 1
        self.sex = sex
        self.color = color
        self.health = 80
        self.hunger = 80
        self.craving = 80
        self.mood = 50
        self.vivacity = 10
        self.cleanliness = 0
        self.upbringing = 0

    def character_selection(self):

        print(f"Type: {self.type_of_animal}\n  Name: {self.name}\n Age: {self.age}\n Sex: {self.sex}\n Color: {self.color}\n "
              f"Health: {self.health}\n Hunger: {self.hunger}\n Craving: {self.craving}\n Mood: {self.mood}\n "
              f"Vivacity: {self.vivacity}\n Cleanliness: {self.cleanliness}\n Upbringing: {self.upbringing}")


Cat = Animal(name, type_of_animal, sex, color)
Cat.character_selection()


















