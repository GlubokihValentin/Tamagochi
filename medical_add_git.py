# Ветка medical
# прописываем все свойства по лечению персонажа - взаимосвязано со здоровьем  и настроением

# self.health = 80     # здоровье  изначально
# self.vivacity = 10     #  бодрость изначально

def medical():
    if (health <= 35 and health > 15) and (vivacity <= 20 and vivacity > 15):
        print('Ваше здоровье ухудшилось,необходимо подлечиться!!')
    if (health <= 15 and health > 5) and (vivacity <= 15 and vivacity > 5):
        print('Вам необходимы стимуляторы!!')
    if (health <= 5 and health > 1) and (vivacity <= 5 and vivacity > 1):
            print('Срочно реанимацию!!')
