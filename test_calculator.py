# https://github.com/zvpp3/Lab11-AR-BG
# Partner 1: Avery Roelofsen
# Partner 2: Braydin Gadouas

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    # Leave your partner's tests here


    ######### Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 4), -8)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(4, 20), 5)
        self.assertEqual(divide(5, 15), 3)


    ######### Partner 2
    # Leave your partner's tests here


    ######### Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)


# Do not touch this
if __name__ == "__main__":
    unittest.main()