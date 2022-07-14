from unittest import TestCase
from class_q import *

class TestFindPairs(TestCase):
    print(":)")
    def test_number_sum(self):
        print(":)")
        expected = {3,5}
        result = (number_sum([-4, 5, 8, 3, 10], 8))
        self.assertEqual(expected, result)

    # def test_two_number_sum(self):
    #     expected = None
    #     result = find_pairs([1, 2, 4, 2, 1, 45, 51, 24], 60)
    #     self.assertEqual(expected, result)
