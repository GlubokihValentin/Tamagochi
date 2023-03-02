import random


class Animal:
    def __init__(self, name, type, sex, color):
        self.name = name
        self.type = type
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



Cat = Animal('Barsik', 'Cat', 'man', 'white')


# def character_selection(self):
#     print(
#         f"Type: {self.type_of_animal}\n  Name: {self.name}\n Age: {self.age}\n Sex: {self.sex}\n Color: {self.color}\n "
#         f"Health: {self.health}\n Hunger: {self.hunger}\n Craving: {self.craving}\n Mood: {self.mood}\n "
#         f"Vivacity: {self.vivacity}\n Cleanliness: {self.cleanliness}\n Upbringing: {self.upbringing}")


listA = [28, 2, 30, 25, 15]
listB = []
event = 0

for i in range(len(listA)):
    p = 0

    for j in range(i + 1):
        p += listA[j]

    listB.append(p)

print(listB)

a = random.randint(1, sum(listA))
print(a)

for i in range(len(listB)):
    if a <= listB[i]:
        event = i + 1
        break

print(event)


def random_events() -> object:
    match event:
        case 1:  # ранение
            print('Oh no! While you were away your pet got hurt! Take him to the vet immediately!')
            Cat.health = 10

        case 2:  # смерть
            print('It is a pity! Your animal has died. Accept our condolences!')
            del Cat  # теперь надо завести нового

        case 3:  # мимо лотка
            print('Oops...your pet went past the tray')
            Cat.cleanliness = 0
            Cat.upbringing = 10

        case 4:  # испортил мебель
            b = random.randint(1, 3)
            if b == 1:
                print('Your pet was playing and accidentally broke a vase with flowers')


            elif b == 2:
                print('Your pet was bored and it scratched the couch')


            else:
                print('Your pet snuck into the closet and scattered all the things')

        case 5:
            print('Recently there was a strong storm and lightning flashed! Your pet is scared, he has a lot of stress')
            Cat.mood = 0
            Cat.health = 40


random_events()