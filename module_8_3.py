class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if is_valid_vin(vin):
            self.__vin = vin
        if is_valid_numbers(numbers):
            self.__numbers = numbers


class IncorrectVinNumber(Exception):
    def __init__(self, message=''):
        self.message = message
        super().__init__(self, message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message='Неверная длина номера'):
        self.message = message
        super().__init__(self, message)


def is_valid_vin(vin):
    if not isinstance(vin, int):
        raise IncorrectVinNumber('Некорректный тип vin номер')
    elif not (1000000 <= vin <= 9999999):
        raise IncorrectVinNumber('Некорректный тип vin номер')
    else:
        return True


def is_valid_numbers(number):
    if not isinstance(number, str):
        raise IncorrectVinNumber('Некорректный тип данных для номеров')
    elif not (len(number) == 6):
        raise IncorrectVinNumber('Неверная длина номера')
    else:
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
