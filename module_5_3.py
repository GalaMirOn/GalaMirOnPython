class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'Мы в {self.name}, едем на {new_floor} этаж')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i, end='  ')
            print()

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __lt__(self, other):
        if not isinstance(other, House):
            print('Ошибка! Классы объектов не совпадают')
            return self
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            print('Ошибка! Классы объектов не совпадают')
            return self
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            print('Ошибка! Классы объектов не совпадают')
            return self
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            print('Ошибка! Классы объектов не совпадают')
            return self
        return self.number_of_floors >= other.number_of_floors

    def __eq__(self, other):
        if not isinstance(other, House):
            print('Ошибка! Классы объектов не совпадают')
            return self
        return self.number_of_floors == other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            print('Ошибка! Классы объектов не совпадают')
            return self
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            print('Ошибка! Количество этажей не целое число! ')
            return self
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        if not isinstance(value, int):
            print('Ошибка! Количество этажей не целое число! ')
            return self
        self = self + value
        return self

    def __iadd__(self, value):
        if not isinstance(value, int):
            print('Ошибка! Количество этажей не целое число! ')
            return self
        self = self + value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print('1  ', h1)
print('2  ', h2)
print('3  ', h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print('4  ', h1)
print('5  ', h1 == h2)
h1 += 10  # __iadd__
print('6  ', h1)
h2 = 10 + h2  # __radd__
print('7  ', h2)
print('8  ', h1 > h2)  # __gt__
print('9  ', h1 >= h2)  # __ge__
print('10 ', h1 < h2)  # __lt__
print('11 ', h1 <= h2)  # __le__
print('12 ', h1 != h2)  # __ne__
