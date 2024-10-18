import unittest
import runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        proba = runner.Runner('проба walk')
        for i in range(10):
            proba.walk()
        self.assertEqual(proba.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        proba = runner.Runner('проба run')
        for i in range(10):
            proba.run()
        self.assertEqual(proba.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        proba_walk = runner.Runner('проба walk')
        proba_run = runner.Runner('проба run')
        for i in range(10):
            proba_walk.walk()
            proba_run.run()
        self.assertNotEqual(proba_walk.distance, proba_run.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        super().__new__(cls)
        cls.all_results = {}
        return cls.all_results

    @classmethod
    def tearDownClass(cls):
        for key in range(len(cls.all_results), 0, -1):
            # print('Забег №', key, cls.all_results[key])
            dict_val = cls.all_results[key]
            cls.assertTrue('Ник', dict_val[len(dict_val)], 'ok')

    def setUp(self):
        first = rt.Runner('Усейн', 10, )
        second = rt.Runner('Андрей', 9)
        third = rt.Runner('Ник', 3)
        return first, second, third

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test__first_tournament(self):
        first, second, third = TournamentTest.setUp(self)
        number_of_test = 1  # Усэйн и Ник
        proba_start = rt.Tournament(90, first, third).start()
        self.all_results[number_of_test] = proba_start

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test__second_tournament(self):
        first, second, third = TournamentTest.setUp(self)
        number_of_test = 2  # Андрей и Ник
        proba_start = rt.Tournament(90, second, third).start()
        self.all_results[number_of_test] = proba_start

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test__third_tournament(self):
        first, second, third = TournamentTest.setUp(self)
        number_of_test = 3  # Усэйн, Андрей и Ник.
        proba_start = rt.Tournament(90, first, second, third).start()
        self.all_results[number_of_test] = proba_start

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test__fourth_tournament(self):
        number_of_test = 4  # Усэйн, Андрей и Ник.
        r1 = rt.Runner('Вася', 11)
        r2 = rt.Runner('Илья', 9)
        r3 = rt.Runner('Арсен', 10)     # бегуны с одинаковой скоростью
        r4 = rt.Runner('Усейн', 10)     # записываются по алфавиту (возрастание)
        r5 = rt.Runner('Андрей', 9)     # 2: Арсен  3: Усейн
        r6 = rt.Runner('Ник', 3)        # 4: Андрей 5: Илья
        run_1 = [r1, r2, r3, r4, r5, r6]
        proba_start= rt.Tournament(90, *run_1).start()
        self.all_results[number_of_test] = proba_start
        self.assertEqual({1: 'Вася', 2: 'Арсен', 3: 'Усейн', 4: 'Андрей', 5: 'Илья', 6: 'Ник'}, proba_start)


if __name__ == '__main__':
    unittest.main()