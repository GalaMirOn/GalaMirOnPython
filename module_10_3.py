from threading import Thread, Lock
from random import randint
from time import sleep

lock1 = Lock()
lock2 = Lock()
son = 0.001

class Bank(Thread):
    def __init__(self, balance = 0, *args, ** kwargs):
        super().__init__(*args, **kwargs)
        self.balance = balance

    def deposit(self):
        for i in range(100):
            if self.balance > 500 and lock1.locked():
                lock1.release()
            dep = randint(50, 500)
            lock2.acquire()
            self.balance = self.balance + dep
            print(f' Пополнение: {dep}. Баланс: {self.balance}')
            lock2.release()
            sleep(son)

    def take(self):
        for i in range(100):
            if not lock1.locked():
                ta = randint(50, 500)
                lock2.acquire()
                print(f' Запрос на {ta}')
                if ta <= self.balance:
                    self.balance = self.balance - ta
                    print(f' Снятие: {ta}. Баланс: {self.balance}')
                else:
                    lock1.acquire()
                    print(' Запрос отклонён, недостаточно средств')
                lock2.release()
            sleep(son)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')