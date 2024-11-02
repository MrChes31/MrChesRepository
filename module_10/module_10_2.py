#наследованные от класса Thread.
# Задача "За честь и отвагу!"

from threading import Thread
from time import sleep


class Knight(Thread):
    #   Атрибут name - имя рыцаря. (str)
    #   Атрибут power - сила рыцаря. (int)

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        # Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
        foes = 100
        days_war = 0

        # При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
        print(f"{self.name}, на нас напали!")
        while foes > 0:  # пока количество врагов больше 0
            foes -= self.power
            sleep(1)
            days_war += 1
            if foes < 0:
                print(f"{self.name} сражается {days_war} день(дня).., осталось 0 воинов.")
            else:
                print(f"{self.name} сражается {days_war} день(дня).., осталось {foes} воинов.")
        print(f"{self.name} одержал победу спустя {days_war} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
