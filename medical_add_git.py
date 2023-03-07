# Ветка medical
# прописываем все свойства по лечению персонажа - взаимосвязано со здоровьем  и настроением

import tamagochi.py

# health = 33     # здоровье  изначально
# vivacity = 10     #  бодрость изначально

@health.setter
def health(self, a):
    self._health = 100


@vivacity.setter
def vivacity(self, f):
    self._vivacity = 100

def medical(health, vivacity):
    if (35 >= health > 15) and (20 >= vivacity > 15):
        print('Ваше здоровье ухудшилось,необходимо подлечиться!!')
    #     тут необходимо просать условие чтобы здоровье и бодрость изменялись

    elif (15 >= health > 5) and (15 >= vivacity > 5):
         print('Вам необходимы стимуляторы!!')
        #     тут необходимо просать условие чтобы здоровье и бодрость изменялись

    elif (5 >= health > 1) and (5 >= vivacity > 1):
         print('Срочно реанимацию!!')
        #     тут необходимо просать условие чтобы здоровье и бодрость изменялись

    elif (45 >= health > 35) and (45 >= vivacity > 35):
         print('Энегретик тебе в помощь,немного приуныл!! или SNIKERS-ni')

    else:    # health > 45 and vivacity > 35
          print("Здоровье в порядке - спасибо подзарядке")
          return self._health


# medical()
