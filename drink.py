

def drink(a):
    if a.is_sleep == False:
            if a.cravity < 20:
                a.cravity += 25
            elif a.cravity < 50:
                a.cravity += 20
            elif a.cravity < 100:
                a.cravity += 5
            else:
                print('Питомец не хочет пить')
    return a.cravity




