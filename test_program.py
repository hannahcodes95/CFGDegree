#testing my program for a simple calc

import unittest
import program

class TestProgram(unittest.TestCase):

    def test_add(self):
        self.assertEqual(program.add(10, 5), 15)
        self.assertEqual(program.add(-10, -5), -15)
        self.assertEqual(program.add(-10, 5), -5)

    def test_subtract(self):
        self.assertEqual(program.subtract(10,5),5)
        (program.subtract(-10, -5), -5)
        (program.subtract(-10, 5), -15)

    def test_multiply(self):
        self.assertEqual(program.multiply(10,5),50)
        (program.subtract(-10, -5), 50)
        (program.subtract(-10, 5), -50)

    def test_division(self):
        self.assertEqual(program.division(10,5),2)
        (program.subtract(-10, -5), 2)
        (program.subtract(-10, 5), -2)

if __name__ == '__main__':
    unittest.main()