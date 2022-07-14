import unittest
from unittest import TestCase
from palindrom import is_palindrome

class TestPalindrom(unittest.TestCase):

    def test_is_palindrome_True(self):
        expected = True
        returned = is_palindrome('Hannah')
        self.assertEqual(expected, returned)

    def test_is_palindrome_False(self):
        expected = False
        returned = is_palindrome('Hanna')
        self.assertEqual(expected, returned)

    def test_is_palindrome_value(self):
        expected = 'String only'
        returned = is_palindrome(1)
        self.assertEqual(expected, returned)


if __name__ == '__main__':
    unittest.main()