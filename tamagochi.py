import random
import time


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


# def features(Cat):
#     if

def init_list():
    listA = [28, 2, 30, 25, 15]
    listB = []

    for i in range(len(listA)):
        p = 0

        for j in range(i + 1):
            p += listA[j]

        listB.append(p)

    print(listB)
    return listB


def init_event():
    c = init_list()
    event = 0

    a = random.randint(1, 100)
    print(a)

    for i in range(len(c)):
        if a <= c[i]:
            event = i + 1
            break

    print(event)
    return event


def random_events(Cat):
    e = init_event()

    match e:
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
            print(
                'Recently there was a strong storm and lightning flashed! Your pet is scared, he has a lot of stress')
            Cat.mood = 0
            Cat.health = 40


def main(Cat):
    random_events(Cat)


while True:  # работает, но так лучше не делать. Переделаем, когда изучим ассинхронность
    b = random.randint(12*3600, 24*3600)
    time.sleep(b)
    main(Cat)
