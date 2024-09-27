class Figure:
    sides_count = 0

    def __init__(self, __color, __sides, filled=True):
        self.__color = __color
        self.__sides = __sides
        self.filled = filled
        # print('init Figure:   цвет:', self.__color, 'sides:', self.__sides, ' закраска:', self.filled)

    def __sides__(self, __sides):
        rebro = __sides
        rebro_list = []
        for i in range(0, 12):
            rebro_list.append(rebro)
        return rebro_list

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        # print('проверка цвета: ', r, g, b)
        if r < 0 or g < 0 or b < 0 or r > 255 or g > 255 or b > 255:
            # print('Ошибка в параметрах цвета: ', r, g, b)
            return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            # print('Цвет изменен на ', self.__color)

    def __is_valid_sides(self, sides):
        if self.sides_count != len(sides):
            return False
        for side in sides:
            if side <= 0 or not isinstance(side, int):
                return False
        return True

    def set_sides(self, *new_sides):
        # print('Вход в set_sides: ', new_sides, len(new_sides))
        if self.sides_count != len(new_sides):
            return
        if self.__is_valid_sides(new_sides):
            if len(new_sides) == 1:
                new_sides = new_sides[0]
            self.__sides = new_sides
        # print('Стороны set: ', self.__sides)

    def get_sides(self):
        # print('Стороны get_sides: ', self.__sides)
        return self.__sides

    def __len__(self):
        sd = self.get_sides()
        # print('len = ', sd)
        if (self.sides_count == 1) and isinstance(self, Circle) and isinstance(sd, int):
            perimetr = sd
        elif self.sides_count == 3 and isinstance(self, Triangle):
            perimetr = sd[0] + sd[1] + sd[2]
        elif self.sides_count == 12 and isinstance(self, Cube):
            if isinstance(sd, int):
                perimetr = 12 * sd
            else:
                perimetr = 12 * sd[0]
        # print('perimetr ', perimetr)
        return perimetr


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        sides_list  = list(sides)
        kol_sides = len(sides_list)
        # print('инит круг', list(sides), len(sides_list))
        if kol_sides != self.sides_count:
            sides = 1
        else:
            sides = sides_list[0]
        if not isinstance(sides, int):
            sides = 1
        super().__init__(color, sides)
        self.__radius = sides / 2 * 3.1416
        # print('радиус: ', self.__radius)

    def get_square(self):
        sq = 3.1416 * self.__radius * self.__radius
        # print('Площадь круга', sq)
        return sq


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *sides):
        # print('инит треугольник ', sides)
        if not len(sides) == 3:
            sides = [1, 1, 1]
        super().__init__(__color, sides)
        # print('Треугольник: ', self.get_sides())

    def get_square(self):
        st = super().__len__() / 2
        sides_list = self.get_sides()
        # print('sides_list', st, sides_list)
        st = (st * (st - sides_list[0]) * (st - sides_list[1]) * (st - sides_list[0])) ** 0.5
        # print('Площадь треугольника: ', st)
        return st


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides[0]
        if not isinstance(sides, int):
            sides = 1
        rebro_list = super().__sides__(sides)
        super().__init__(color, rebro_list)




circle1 = Circle((200, 200, 100), 10, 17)  # ошибка количества сторон
print(vars(circle1))
circle1 = Circle((200, 200, 100), 10)
print(vars(circle1))
print(circle1.get_color())
print(circle1.get_square())
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
circle1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())

# Проверка периметра (круга), это и есть длина:
print('окружность ', len(circle1))
circle1.set_sides(88)  # Изменится
print(circle1.get_sides())

triangle = Triangle((120, 50, 80), 15, 20, 25, 30)
print(vars(triangle))
print('perimetr ', len(triangle))
print(triangle.get_square())
triangle = Triangle((120, 50, 80), 15, 20, 25)
print(vars(triangle))
print('perimetr ', len(triangle))
print(triangle.get_square())

cube1 = Cube((222, 35, 130), 6, 7, 8)
print(vars(cube1))
print(cube1.get_sides())
print(len(cube1))

cube1 = Cube((222, 35, 130), 4)
print(vars(cube1))
print(cube1.get_sides())
print(len(cube1))
# print(dir(cube1))
# print(vars(cube1))