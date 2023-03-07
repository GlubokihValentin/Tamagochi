import datetime as date
import sys, os , random
from interface import listOfAnimal as list, indexOfListAnimal as index


# a = date.datetime.now().time().second
# print(a)
# b = date.datetime.now().time().second
# print(b)
def wallAndHead(list[index]):
    try:
        n = 1
        a = 1
        q = date.datetime.now().time().minute
        q1 = date.datetime.now().time().second
        while n == 1:
            print('У меня есть игра которая тебе понравится =)\n'
                  'Хочешь в нее сыграть?\n'
                  '1 - Да '
                  '2- Нет')
            gameWallAndHead = int(input())
            match(gameWallAndHead):
                case 1:
                    print('Бряк об стену')
                    a = a + 1
                case 2:
                    print('Очень жаль, тебе бы игра понравилась')
                    n = 0
                    play(list[index])
                    break
            if a == 7:
                print('Сорри наступила смерть')
                newq = date.datetime.now().time().minute
                newq1 = date.datetime.now().time().second
                if (newq - q) == 1 :
                    print(f'Мы играли {newq - q} минуту')
                    break
                elif (newq - q) > 1 and (newq - q) < 5 :
                    print(f'Мы играли {newq - q} минуты')
                    break
                elif (newq - q) < 1:
                    print(f'Мы играли всего лишь {newq1 - q1} секунды')
                    break
                break
    except ValueError:
        wallAndHead(list[index])

def footbol(list[index]):
    try:
        nFootbol = 1
        aFootbol = 1
        # testNumber = 50 # удалить потом
        while nFootbol == 1:
            print('Давай играть в футбол!\n'
                ' Напиши 1 -Да, 2 - Нет')
            gameFotbool = int(input())
            match(gameFotbool):
                case 1:
                    ran = random.randint(1, 13)
                    if list[index].mood <= 100:
                        if ran == 5 or ran == 7:
                            print('Я пропустил мяч, какая печаль =(')
                            list[index].mood -= 5
                            print(f'Произошло уменьшение шкалы счастья(mood) вашего питомца до {list[index].mood}')
                        elif ran != 5 and ran != 7:
                            print('Ура!!! Я поймал мяч')
                            # tamagochi.a.mood = tamagochi.a.mood + 5
                            if list[index].mood < 100:
                                list[index].mood += 5
                                print(f'Произошло увеличение шкалы счастья(mood) вашего питомца  до {list[index].mood}')
                    if list[index].mood == 100:
                        print(f'Шкала счастья(mood) вашего питомца {list[index].mood}\n'
                              f'Если хотите можете продолжить играть')
                case 2:
                    print('Если хочешь, мы можем сыграть с тобой во что нибудь другое')
                    nFootbol = 0
                    play(list[index])
                    break
    except ValueError:
        footbol(list[index])

def hockey(list[index]):
    try:
        nHokey = 1
        aHokey = 1
        # testNumber = 50  # удалить потом
        while nHokey == 1:
            print('Я хочу сыграть с тобой в хокей!\n'
                            'Мы будем играть!?')
            print("1 - Да"
              " 2 - Нет")
            hokeyGame = int(input())
            match(hokeyGame):
                case 1:
                    ran = random.randint(1, 13)
                    if list[index].mood <= 100:
                        if ran == 5 or ran == 7:
                            print('Я пропустил шайбу, какая печаль =(')
                            list[index].mood -= 5
                            print(f'Произошло уменьшение шкалы счастья(mood) вашего питомца до {list[index].mood}')
                        elif ran != 5 or ran != 7:
                            print('Ура!!! Я поймал шайбу')
                            if list[index].mood < 100:
                                list[index].mood += 5
                                print(f'Произошло увеличение шкалы счастья(mood) вашего питомца  до {list[index].mood}')
                    if list[index].mood == 100:
                        print(f'Шкала счастья(mood) вашего питомца {list[index].mood}\n'
                              f'Если хотите можете продолжить играть')
                case 2:
                    print('Если хочешь, мы можем сыграть с тобой во что нибудь другое!')
                    nHokey = 0
                    play(list[index])
                    break
    except ValueError:
        hockey(list[index])

def play(list[index]):# в скобках написать tamagjchi.a
    try:
        print(f'{tamagjchi.a}, готов с тобой сыграть!!!\n' # дописать имя животного в начале {tamagochi.a}
          f'Выбери какая игра тебе более интересна :\n'
          f'1 - Футбол\n2 - Хоккей\n3 - Бряк\n0 - Выйти из меню')
        game = int(input())
        match(game):
            case 1:
                footbol(list[index])
            case 2:
                hockey(list[index])
            case 3:
                wallAndHead(list[index])
            case 0:
                print('Выход в основное меню')
    except ValueError:
        play(list[index])
