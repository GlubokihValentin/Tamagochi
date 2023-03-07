# Ветка medical
# прописываем все свойства по лечению персонажа - взаимосвязано со здоровьем  и настроением

# import tamagochi

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
        print(
            f"Type: {self.type_of_animal}\n  Name: {self.name}\n Age: {self.age}\n Is_male: {self.is_male}\n Color: {self.color}\n "
            f"Health: {self.health}\n Hunger: {self.hunger}\n Craving: {self.craving}\n Mood: {self.mood}\n "
            f"Vivacity: {self.vivacity}\n Cleanliness: {self.cleanliness}\n Upbringing: {self.upbringing}\n Is_sleep: {self.is_sleep}")


# Cat = Animal(name, type_of_animal, sex, color)
# Cat.character_selection()
class Cat_Dog(Animal):
    def __init__(self, name, type_of_animal, is_male, color):
        super().__init__(name, type_of_animal, is_male, color)


Kitten = Cat_Dog("Barsik", "Cat", "male", "black")
print(Kitten.name)



# health = 33     # здоровье  изначально
# vivacity = 10     #  бодрость изначально

def medical(health, vivacity):
    if (35 >= health > 15) and (20 >= vivacity > 15):
        print('Ваше здоровье ухудшилось,необходимо подлечиться!!')
    #     тут необходимо просать условие чтобы здоровье и бодрость изменялись

    elif (15 >= health > 5) and (15 >= vivacity > 5):
         print('Вам необходимы стимуляторы!!')
        #     тут необходимо просать условие чтобы здоровье и бодрость изменялись

    elif (5 >= health > 1) and (5 >= vivacity > 1):
         print('Срочно реанимацию!!')
        #     тут необходимо просать условие чтобы здоровье и бодрость изменялись

    elif (45 >= health > 35) and (45 >= vivacity > 35):
         print('Энегретик тебе в помощь,немного приуныл!! или SNIKERS-ni')

    else:    # health > 45 and vivacity > 35
          print("Здоровье в порядке - спасибо подзарядке")
          # return self._health


medical(Kitten.health, Kitten.vivacity)
