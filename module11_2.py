from datetime import date, time
import inspect

class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self


class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self


class Pegasus(Horse, Eagle):

    def __init__(self):
        super().__init__()
        # print(self.x_distance, self.sound)
        Eagle.__init__(self)


    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
        return self

    def get_pos(self):
        koord = (self.x_distance, self.y_distance)
        return koord

    def voice(self):
        print(self.sound)


p1 = Pegasus()
# print(p1.get_pos())
p1.move(10, 15)
# print(p1.get_pos())
p1.move(-5, 20)
# print(p1.get_pos())
#p1.voice()

def introspection_info(obj):
    print('Тип объекта:', type(obj))
    print('Методы и аргументы:')
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        print(attr_name, type(attr))

    print('Это класс?',inspect.isclass(obj))

    print('Это функция?', inspect.isfunction(obj))
    print('Вызвыаемый объект?', callable(obj))
    print('Откуда: ', inspect.getmodule(obj))


number_info = introspection_info(42)
print(number_info)

str_info = introspection_info('Солнце')
print(str_info)

# introspection_info(p1)
# introspection_info(Pegasus)
# introspection_info(p1.move(5,5))
#
# lesson_date = date.today()
# print('Дата:', lesson_date)
# introspection_info(lesson_date)
#
# lesson_time = time(17,24,10)
# print('Время:', lesson_time)
# introspection_info(lesson_time)