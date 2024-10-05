def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        if type(num) == 'list':
            personal_sum(num)
        try:
            result += num
        except TypeError:
            incorrect_data += 1
            print('Некорректный тип данных для подсчёта суммы - ', num)
    return result, incorrect_data

def calculate_average(numbers):
    try:
        summa, incorrect_data = personal_sum(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try:
        srednee = summa / (len(numbers) - incorrect_data)
    except ZeroDivisionError as exp:
        srednee = 0
    return srednee


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать