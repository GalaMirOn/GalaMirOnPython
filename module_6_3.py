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
# print(p1.x_distance, p1.y_distance, p1.sound)
# print(Pegasus.mro())
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
