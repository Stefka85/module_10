from threading import Thread
import time


# Создание класса
class Knight(Thread):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__()

    def power(self, int):
        pass

    def name(self, str):
        pass

# Запуск потоков и остановка текущего

    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name} на нас напали!')
        while enemies > 0:
            enemies -= self.power
            days += 1
            print(f'{self.name} сражается {days}, осталось {enemies} воинов')
            time.sleep(1)
            if enemies == 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thread_1 = first_knight
thread_2 = second_knight

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

# Вывод строки об окончании сражения
print(f'Все битвы закончились!')



