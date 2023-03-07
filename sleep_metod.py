import time
import datetime


def sleep_metod(self):
    time_1 = datetime.datetime.now()
    if self.vivacity >= 30 and 6 < time_1 <= 22:
        print('Я не хочу спать!')
        return

    while self.vivacity <= 95 or time_1.hour < 7:
        self.vivacity += 1
        time.sleep(0.1)
        print('Спокойной ночи, я пошел спать...')
        print(self.vivacity)
        time_1 = datetime.datetime.now()
