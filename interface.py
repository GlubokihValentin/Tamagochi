# import feed, drink, game, cleaning, sleep_metod, medical, nurture, achiv, create, change
import tamagochi

listofAnimal = []
print('Нажмите 8, чтобы создать своего питомца')
print('Нажмите 1, чтобы покормить')
print('Нажмите 2, чтобы дать попить')
print('Нажмите 3, чтобы поиграть')
print('Нажмите 4, чтобы убрать за питомцем')
print('Нажмите 5, чтобы уложить спать')
print('Нажмите 6, чтобы дать лекарства')
print('Нажмите 7, чтобы воспитать')
print('Нажмите 0, чтобы посмотреть шкалы')
print('Нажмите 9, чтобы сменить животное')
choose = input()
match choose:
    case 1:
        feed.feed()
    case 2:
        drink.drink()
    case 3:
        game.play()
    case 4:
        cleaning.cleaning()
    case 5:
        sleep_metod.sleep()
    case 6:
        medical.medical()
    case 7:
        nurture.nurture()
    case 0:
       achiv.set_properties()
    case 8:
        create()
    case 9:
        change()



def create():
    type_of_animal = ['кот', 'собака', 'кролик', 'хомяк', 'дракон']
    kindOfAnimal = None
    print('Нажмите 1, если это кот')
    print('Нажмите 2, если это собака')
    print('Нажмите 3, если это кролик')
    print('Нажмите 4, если это хомяк')
    print('Нажмите 5, если это дракон')
    yourAnimal = input()


    is_male = ['мальчик', 'девочка']
    gender = None
    print('Нажмите 0, чтобы выбрать питомца-девочку')
    print('Нажмите 6, чтобы выбрать питомца-мальчика')
    genderOfAnimal = input()

    color = ['чёрный', 'белый', 'рыжий', 'розовый', 'жёлтый', 'зелёный', 'голубой']
    hair = None
    print('Нажмите 7, если хотите питомца чёрного цвета')
    print('Нажмите 8, если хотите питомца белого цвета')
    print('Нажмите 9, если хотите питомца рыжего цвета')
    print('Нажмите 10, если хотите питомца розового цвета')
    print('Нажмите 11, если хотите питомца жёлтого цвета')
    print('Нажмите 12, если хотите питомца зелёного цвета')
    print('Нажмите 11, если хотите питомца голубого цвета')
    colorOfAnimal = input()

    match yourAnimal:
        case 1:
            kindOfAnimal = type_of_animal[0]
        case 2:
            kindOfAnimal = type_of_animal[1]
        case 3:
            kindOfAnimal = type_of_animal[2]
        case 4:
            kindOfAnimal = type_of_animal[3]
        case 5:
            kindOfAnimal = type_of_animal[4]

    match genderOfAnimal:
        case 0:
            gender = is_male[1]
        case 6:
            gender = is_male[0]

    match colorOfAnimal:
        case 7:
            hair = color[0]
        case 8:
            hair = color[1]
        case 9:
            hair = color[2]
        case 10:
            hair = color[3]
        case 11:
            hair = color[4]
        case 12:
            hair = color[5]
        case 13:
            hair = color[6]
            
    print('Введите имя питомца: ')
    nameOfAnimal = input()

    listofAnimal.append(tamagochi.Animal(nameOfA, typeOfA, genderOfA, colorOfA))

def change():
    indexOflistOfNewAnimal = new tamagochi.Animal(nameOfA, typeOfA, genderOfA, colorOfA)