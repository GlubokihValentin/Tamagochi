type_of_animal = input("Введите вид персонажа: ")
name = input("Введите имя персонажа: ")
sex = input("Введите пол персонажа: ")
color = input("Введите цвет персонажа: ")


class Animal:
    def __init__(self, name, type_of_animal, is_male, color):
        self.name = name
        self.type_of_animal = type_of_animal
        self.age = 1
        self.is_male = is_male
        self.color = color
        self._health = 80
        self._hunger = 80
        self._craving = 80
        self._mood = 50
        self._vivacity = 10
        self._cleanliness = 0
        self._upbringing = 0
        self._is_sleep = False

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, a):
        self._health = a

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, b):
        self._hunger = b

    @property
    def craving(self):
        return self._craving

    @craving.setter
    def craving(self, c):
        self._craving = c

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, e):
        self._mood = e

    @property
    def vivacity(self):
        return self._vivacity

    @vivacity.setter
    def vivacity(self, f):
        self._vivacity = f

    @property
    def cleanliness(self):
        return self._cleanliness

    @cleanliness.setter
    def cleanliness(self, g):
        self._cleanliness = g

    @property
    def upbringing(self):
        return self._upbringing

    @upbringing.setter
    def upbringing(self, h):
        self._upbringing = h

    @property
    def is_sleep(self):
        return self._is_sleep

    @is_sleep.setter
    def is_sleep(self, h):
        self._is_sleep = h

    
    def character_selection(self):

        print(f"Type: {self.type_of_animal}\n  Name: {self.name}\n Age: {self.age}\n Is_male: {self.is_male}\n Color: {self.color}\n "
              f"Health: {self.health}\n Hunger: {self.hunger}\n Craving: {self.craving}\n Mood: {self.mood}\n "
              f"Vivacity: {self.vivacity}\n Cleanliness: {self.cleanliness}\n Upbringing: {self.upbringing}\n Is_sleep: {self.is_sleep}")


Cat = Animal(name, type_of_animal, sex, color)
Cat.character_selection()


















