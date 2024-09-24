class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Возможные цвета

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_harsepower(self):
        return f'Мощность: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_harsepower())
        print(self.get_color())
        print('Владелец: ', self.owner)

    def set_color(self, new_color):
        for _color in self.__COLOR_VARIANTS:
            if new_color.upper() == _color.upper():
                self.color = new_color
                return
        print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
