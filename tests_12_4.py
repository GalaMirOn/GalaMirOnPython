import unittest
import rt_with_exceptions as runner
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r1 = runner.Runner('Василий', -7)
            r1.walk()
            logging.info('"test_walk" выполнен успешно')
            # self.assertEqual(proba.distance, 50)
        except Exception:
            logging.exception('Неверная скорость для Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r2 = runner.Runner(78)
            r2.run()
            logging.info('"test_run" выполнен успешно')
        except Exception:
            logging.exception('Неверный тип данных для объекта Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        proba_walk = runner.Runner('проба walk')
        proba_run = runner.Runner('проба run')
        for i in range(10):
            proba_walk.walk()
            proba_run.run()
        self.assertNotEqual(proba_walk.distance, proba_run.distance)

if __name__ == '__main__':
    unittest.main()