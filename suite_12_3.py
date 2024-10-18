import unittest
import tests_12_3



zabegST = unittest.TestSuite()
zabegST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
zabegST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(zabegST)
