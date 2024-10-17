import unittest
import runner_and_tournament as rt
# import test12 as rt


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().__new__(cls)
        cls.all_results = {}
        return cls.all_results

    @classmethod
    def tearDownClass(cls):
        for key in range(len(cls.all_results), 0, -1):
            print('Забег №', key, cls.all_results[key])
            dict_val = cls.all_results[key]
            cls.assertTrue('Ник', dict_val[len(dict_val)])

    def setUp(self):
        first = rt.Runner('Усейн', 10, )
        second = rt.Runner('Андрей', 9)
        third = rt.Runner('Ник', 3)
        return first, second, third

    def test_start(self):
        first, second, third = TournamentTest.setUp(self)
        number_of_test = 1  # Усэйн и Ник
        proba_start = rt.Tournament(90, first, third).start()
        self.all_results[number_of_test] = proba_start

        number_of_test += 1  # Андрей и Ник
        proba_start = rt.Tournament(90, second, third).start()
        self.all_results[number_of_test] = proba_start

        number_of_test += 1  # Усэйн, Андрей и Ник.
        proba_start = rt.Tournament(90, first, second, third).start()
        self.all_results[number_of_test] = proba_start

        number_of_test += 1  # Усэйн, Андрей и Ник.
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
