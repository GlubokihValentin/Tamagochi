def nurture():
    while upbringing == 80:
        a = input(print('Ваш питомец плохо себя ведёт, чтобы ткнуть его мордой в лоток, '
                        'нажмите "T"'))
        if a == "T":
            upbringing = 0
        else:
            print('Вы ввели неправильное значение')
