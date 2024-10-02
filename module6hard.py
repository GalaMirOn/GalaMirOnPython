class Figure:
    sides_count = 0

    def __init__(self, __color: list, *__sides: int):
        self.__color = [*__color] if self.__is_valid_color(*__color) else [0, 0, 0]
        if self.__is_valid_sides(*__sides):
            self.__sides = [*__sides]
        else:
            # print('данные некорректны: ', __sides)
            self.__sides = [1] * self.sides_count

        if len(__sides) != self.sides_count:
            if len(__sides) == 1 and self.sides_count == 12:
                self.__sides = [*__sides] * 12
            else:
                self.__sides = [1] * self.sides_count
        self.filled = False
        # print('Выход из инита Фигуры ')
        # print(vars(self))

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *color):
        r, g, b = [*color]
        # print('%%%  проверка цвета: ', r, g, b) a, b, c = self.get_sides()
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r < 0 or g < 0 or b < 0 or r > 255 or g > 255 or b > 255:
                #print('Ошибка в параметрах цвета: ', r, g, b)
                return False
        else:
            return False
        return True

    def set_color(self, *color):
        if self.__is_valid_color(*color):
            self.__color = [*color]
            # print('###Цвет изменен на ', *color)

    def __is_valid_sides(self, *sides: list):
        #print('sides', [*sides], sides)
        sd = [*sides]
        if len(sd) != self.sides_count: return False

        for side in sd:
            if side <= 0 or not isinstance(side, int):
                return False
        # print('Проверка пройдена!')
        return True

    def set_sides(self, *new_sides):
        # print('**&&  Вход в set_sides: ', *new_sides, len(new_sides))
        ns = [*new_sides]
        if self.sides_count != len(ns):
            # self.__sides = [*new_sides]
            return
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]
        # else:
        #     print('Значения сторон некорректны!')
        return

    def get_sides(self):
        # print('Стороны get_sides: ', self.__sides)
        return self.__sides

    def __len__(self):
        # print('LEN = ', sum(self.__sides), ' стороны ', self.__sides)
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color: list, *sides: int):
        super().__init__(__color, *sides)
        okr = self.get_sides()
        self.__radius = okr[0] / 2 / 3.1416

    def get_square(self):
        # okr = self.get_sides()
        # a = okr[0]
        sq = 3.1416 * self.__radius * self.__radius
        # print('Площадь круга', sq)
        return sq

    def set_sides(self, *new_sides):
        # print('Circle sides', *new_sides)
        super().set_sides(*new_sides)
        okr = [*new_sides]
        # print('okr=', okr)
        self.__radius = okr[0] / 2 / 3.1416


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # print('Треугольник: ', self.get_sides())

    def get_square(self):
        a, b, c = super().get_sides()
        st = 0.5 * (a + b + c)
        st = (st * (st - a) * (st - b) * (st - c)) ** 0.5
        # print('Площадь треугольника: ', st)
        return st


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, *sides):
        # print('кубик ', color, *sides)
        super().__init__(color, *sides)
        # self._set_sides(*sides)

    def set_sides(self, *new_sides):
        st = [*new_sides]
        # print('set_sides Cube ', st)
        if len(new_sides) != self.sides_count:
            st = st * 12
        super().set_sides(*st)
        # print('отладка ', vars(self))
        # print('set_sides Cube rezult', st)

    def get_volume(self):
        sides = super().get_sides()
        volume = sides[0] ** 3
        # print('volume ', sides[0], volume)
        return volume

    def _get_sides(self):
        # print('Стороны _get_sides: ', self.__sides)
        return self.__sides


def test_circle():
    circle1 = Circle([255, 255, 255], 17)
    print(vars(circle1))
    circle1 = Circle([7, 8, 9], 10, 19)
    print(vars(circle1))
    print(circle1.get_color())
    print(circle1.get_square())
    print('окружность ', len(circle1))
    circle1.set_sides(88)  # Изменится
    print(vars(circle1))
    print('окружность ', len(circle1))
    print(circle1.get_sides())
    print(circle1.get_square())

def test_triangle():
    print('***** ТРЕУГОЛЬНИКИ *****')
    triangle = Triangle((120, 50, 90), 15, -20, 25, 30)
    print(vars(triangle))
    print('LEN perimetr ', len(triangle))
    print('площадь треугольника = ', triangle.get_square())
    triangle = Triangle((120, 50, 80), 15, 20, 25)
    print('perimetr ', len(triangle))
    print(vars(triangle))
    triangle.set_sides(4, 5, 2)
    print('perimetr ', len(triangle))
    print('площадь треугольника = ', triangle.get_square())


def test_cube():
    print('***** КУБИКИ *****')
    cube1 = Cube([222, 35, 130], 6)
    print(vars(cube1))
    print(cube1.get_sides())
    print('периметр куба ', len(cube1))
    print('объем куба ', cube1.get_volume())
    cube1 = Cube([222, 35, 130], 4)
    print(vars(cube1))
    print(cube1.get_sides())
    print(len(cube1))
    print(cube1.get_volume())
    cube1 = Cube([222, 35, 130], 6)
    print(cube1.set_sides(9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9))
    # print(dir(cube1))
    print(vars(cube1))
    print(cube1.set_sides(2))
    print(cube1.get_sides())


def test_color():
    circle1 = Circle([255, 255, 255], 17)
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    circle1.set_color(300, 70, 15)  # Не изменится
    print(circle1.get_color())


if __name__ == '__main__':
    test_circle()
    test_triangle()
    test_cube()
    test_color()
