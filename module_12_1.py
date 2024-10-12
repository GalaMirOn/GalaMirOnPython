import unittest
import runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        proba = runner.Runner('проба walk')
        for i in range(10):
            proba.walk()
        self.assertEqual(proba.distance, 50)

    def test_run(self):
        proba = runner.Runner('проба run')
        for i in range(10):
            proba.run()
        self.assertEqual(proba.distance, 100)

    def test_challenge(self):
        proba_walk = runner.Runner('проба walk')
        proba_run = runner.Runner('проба run')
        for i in range(10):
            proba_walk.walk()
            proba_run.run()
        self.assertNotEqual(proba_walk.distance, proba_run.distance)

if __name__ == '__main__':
    unittest.main()