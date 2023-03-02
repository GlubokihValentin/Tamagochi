import datetime as date
import tamagochi


def footbol():
    nFootbol = 1
    aFootbol = 1
    #testNumber = 50 # удалить потом
    while nFootbol == 1 :
        print('Давай играть в футбол!\n'
            ' Напиши 1 -Да, 2 - Нет')
        gameFotbool = int(input())
        match(gameFotbool):
            case 1 :
                print('Game')
                tamagochi.a.mood += 5
                #testNumber += 5
                print(f'Шкала mood равна {tamagochi.a.mood}')
                if testNumber == 100:
                    testNumber = 100
                    print(f'Я устал играть давай передохнем, шкала mood равна {tamagochi.a.mood}')
                    nFootbol = 0
                    play()
            case 2 :
                print('No Game')
                nFootbol = 0
                play()
                break

def hockey():
    nHokey = 1
    aHokey = 1
    #testNumber = 50  # удалить потом
    while nHokey == 1:
        print('Я хочу сыграть с тобой в хокей!\n'
                        'Мы будем играть!?')
        print("1 - Да"
          " 2 - Нет")
        hokeyGame = int(input())
        match(hokeyGame):
            case 1 :
                print('Game')
                tamagochi.a.mood += 5
                #testNumber += 5
                print(f'Шкала mood равна {tamagochi.a.mood}')
                if testNumber == 100:
                    testNumber = 100
                    print(f'Я устал играть давай передохнем, шкала mood равна {tamagochi.a.mood}')
                    nHokey = 0
                    play()
            case 2 :
                print('No Game')
                nHokey = 0
                play()
                break

# def wallAndHead():
#     n = 1
#     a = 1
#     while n == 1:
#         print('У меня есть игра которая тебе понравится =)\n'
#               'Хочешь в нее сыграть?\n'
#               '1 - Да '
#               '2 - Нет')
#         gameWallAndHead = int(input())
#         match(gameWallAndHead):
#             case 1:
#                 print('Бряк об стену')
#                 a = a + 1
#             case 2:
#                 print('Очень жаль, тебе бы игра понравилась')
#                 n = 0
#                 break
#         if a == 5:
#             print('Сорри наступила смерть')
#             break
#
def wallAndHead():
    n = 1
    a = 1
    q = date.datetime.now().time().minute
    q1 = date.datetime.now().time().second
    #testNumber = 50  # удалить потом
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
                tamagochi.a.mood += 5
                #testNumber += 5
                print(f'Шкала mood равна {tamagochi.a.mood}')
                if testNumber == 100:
                    testNumber = 100
                    print(f'Я устал играть давай передохнем, шкала mood равна {tamagochi.a.mood}')
                    n = 0
                    play()
            case 2:
                print('Очень жаль, тебе бы игра понравилась')
                print(f'Шкала mood равна {tamagochi.a.mood}')
                n = 0
                play()
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

def play(tamagjchi.a):   # в скобках написать tamagjchi.a
    print(f'{tamagochi.a}, давай с тобой сыграем!!!\n' # дописать имя животного в начале {tamagochi.a}
          f'Выбери какая игра тебе более интересна :\n'
          f'1 - Футбол\n2 - Хоккей\n3 - Бряк\n0 - Выйти из меню')
    game = int(input())
    match(game):
        case 1:
            footbol()
        case 2:
            hockey()
        case 3:
            wallAndHead()
        case 0:
            print('Выход в основное меню')

play()