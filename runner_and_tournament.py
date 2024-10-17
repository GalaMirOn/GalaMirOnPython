class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed  # * 2  исправлено Мироновской Г.Ю.

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            finish = []  # добавлено Мироновской Г.Ю.
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finish.append((participant.distance, participant))
            if len(finish) > 1:                                     # добавлено Мироновской Г.Ю.
                finish.sort(key=lambda x: x[1].name, reverse=False) # добавлено Мироновской Г.Ю.
                finish.sort(key=lambda x: x[0], reverse=True)       # добавлено Мироновской Г.Ю.
            for iter in finish:                                     # добавлено Мироновской Г.Ю.
                finishers[place] = iter[1].name                     # добавлено Мироновской Г.Ю.
                place += 1
                iter[1].distance = 0                                # добавлено Мироновской Г.Ю.
                self.participants.remove(iter[1])
        return finishers


if __name__ == '__main__':                                          # добавлено Мироновской Г.Ю.
    r1 = Runner('Вася', 11)                             # для сортировки бегунов с одинаковой скоростью
    r2 = Runner('Илья', 9)                              # по алфавиту
    r3 = Runner('Арсен', 10)
    r4 = Runner('Усейн', 10)
    r5 = Runner('Андрей', 9)
    r6 = Runner('Ник', 3)

    r7 = Runner('Усейн', 10)            # вариант как в задании
    r8 = Runner('Андрей', 9)            #
    r9 = Runner('Ник', 3)               #

    all_results = {}
    number_of_starts = 1
    run_1 = [r1, r2, r3]
    run_2 = [r4, r5, r6]
    run_4 = [r7, r8, r9]
    run_3 = [r1, r2, r3, r4, r5, r6]
    t = Tournament(100,  *run_1)
    all_results[number_of_starts]= t.start()
    number_of_starts += 1
    t = Tournament(100,  *run_2)
    all_results[number_of_starts]= t.start()
    number_of_starts += 1
    t = Tournament(100,  *run_3)
    all_results[number_of_starts]= t.start()
    number_of_starts += 1
    t = Tournament(100, *run_4)
    all_results[number_of_starts] = t.start()
    for key in all_results:
        print('Забег №', key, all_results[key])