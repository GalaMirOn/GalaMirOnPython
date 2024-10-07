from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, power, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.power = power
        self.vragi = 100
        print(f'{self.name},на нас напали!')

    def run(self):
        rang = int(100 / self.power)
        if 100 % self.power != 0:
           rang += 1

        for i in range(rang):
            time.sleep(1)
            self.vragi = self.vragi - self.power
            if self.vragi > 0:
                print(f"{self.name} сражается {i + 1}-й день, осталось {self.vragi} воинов")
            else:
                print(f"{self.name} сражается {i + 1}-й день, осталось 0 воинов")
                print(f"{self.name} одержал победу спустя {i + 1} дней!")


knight_1 = Knight('Sir Lancelot', 10)
knight_2 = Knight('Sir Galahad', 20)
knight_3 = Knight('Maior Dobrynja Nikitich', 27)
knight_4 = Knight('General Ilja Murometc', 34)

knight_1.start()
knight_2.start()
knight_3.start()
knight_4.start()

knight_1.join()
knight_2.join()
knight_3.join()
knight_4.join()

print('Все битвы закончились!')