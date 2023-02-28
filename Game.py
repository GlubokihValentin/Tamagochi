def footbol():
    print('Давай играть в футбол!\n'
          ' Напиши 1 -Да, 2 - Нет')
    gameFotbool = int(input())
    match(gameFotbool):
        case 1 :
            print('Game')
        case 2 :
            print('No Game')
def hockey():
    print('Я хочу сыграть с тобой в хокей!\n'
                        'Мы будем играть!?')
    print("1 - Да"
          "2 - Нет")
    hokeyGame = int(input())
    match(hokeyGame):
        case 1 :
            print('Game')
        case 2 :
            print('No Game')


hockey()