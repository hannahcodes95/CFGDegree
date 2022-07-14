import unittest
from unittest import TestCase
from square_num import square_num

class TestPalindrom(unittest.TestCase):

    def test_square_num_True(self):
        expected = ([1])
        returned = square_num([1])
        self.assertEqual(expected, returned)

    def test_square_num_Negative(self):
        expected = ([1])
        returned = square_num([-1])
        self.assertEqual(expected, returned)



if __name__ == '__main__':
    unittest.main()