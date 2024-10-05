# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


# Замыкание:
def get_advanced_writer(file_name):
    # file = open(file_name, 'a', encoding='utf-8')

    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='utf-8')
        for elem in data_set:
            if isinstance(elem, list) or isinstance(elem, tuple):
                elem = (' '.join(map(str, elem)))
            elif isinstance(elem, int) or isinstance(elem, float):
                elem = str(elem)
            print(elem)
            file.write(elem + '\n')
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        self.fortuna = choice(self.words)
        return self.fortuna


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть', 'Ещё не знаю', 'Надеюсь', 'Да нет, наверное')
for i in range(12):
    print(first_ball(), end = '. ')

