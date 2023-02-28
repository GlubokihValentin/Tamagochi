def cleaning():
    while cleanliness == 80:
        a = input(print('Ваш питомиц нагадил кучу выше Эйфилевой башни, нажмите "U" чтоб убрать '
                        'за шерстяным'))
        if a == "U":
            cleanliness = 0
        else:
            print('Вы ввели неправильное значение')
