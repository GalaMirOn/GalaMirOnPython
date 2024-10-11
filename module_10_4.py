import time
from queue import Queue
import random
from threading import Thread


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def run(self):
        son = random.randint(2, 15)
        time.sleep(son)
        print(f'{self.name} попробовал(а) {son} пирожков')


class Cafe():

    def __init__(self, tables=[]):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, guests):  # прием гостей *guests
        for stol in range(len(cafe.tables)):
            self.tables[stol].guest = guests[stol]
            print(self.tables[stol].guest.name, 'сел(а) за стол номер', self.tables[stol].number)
            self.tables[stol].guest.start()
        number_in_ochered = 0
        for i in range(stol + 1, len(guests)):
            cafe.queue.put(guests[i])
            number_in_ochered += 1
            print(guests[i].name, 'в очереди с номером ', number_in_ochered)

    def discuss_guests(self):  # обслуживание гостей
        if not cafe.queue.empty():
            free_table = 0
        else:
            free_table = len(cafe.tables) - len(guests)

        while not cafe.queue.empty() or free_table != len(self.tables):
            for table in self.tables:
                if table.guest != None and not table.guest.is_alive():
                    print(f'{table.guest.name} за столом {table.number} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    free_table += 1
                    if not cafe.queue.empty():
                        table.guest = cafe.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()
                        free_table -= 1


cafe = Cafe()
num = [1, 2, 3, 4, 5]
cafe = Cafe([Table(number=number, guest=None) for number in num])
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]
cafe.guest_arrival(guests)
cafe.discuss_guests()
for guest in guests:
    guest.join()
