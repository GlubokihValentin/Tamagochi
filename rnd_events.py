import random
import time
from interface import listOfAnimal as animals, indexOfAnimal as index


Pet = animals[index]


# def features(Pet):
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


def random_events(Pet):
    e = init_event()

    match e:
        case 1:  # ранение
            print('Oh no! While you were away your pet got hurt! Take him to the vet immediately!')
            Pet.health = 10

        case 2:  # смерть
            print('It is a pity! Your animal has died. Accept our condolences!')
            del Pet  # теперь надо завести нового

        case 3:  # мимо лотка
            print('Oops...your pet went past the tray')
            Pet.cleanliness = 0
            Pet.upbringing = 10

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
            Pet.mood = 0
            Pet.health = 40


def main(Pet):
    random_events(Pet)


while True:  # работает, но так лучше не делать. Переделаем, когда изучим ассинхронность
    b = random.randint(12*3600, 24*3600)
    time.sleep(b)
    main(Pet)
