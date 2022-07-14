import unittest
from unittest import TestCase
from ATM import *
from unittest import mock

class TestATM(TestCase):
    def test_authenticate_pin(self):
        expected = True
        returned = authenticate_pin(1234,1234)
        self.assertEqual(expected,returned)
        expected = False
        returned = authenticate_pin(0000, 1234)
        self.assertEqual(expected, returned)
        expected = False
        returned = authenticate_pin('hello', 1234)
        self.assertEqual(expected, returned)

    def test_balance_enquiry(self):
        expected = 1000
        returned = balance_enquiry()
        self.assertEqual(expected,returned)

    @mock.patch('ATM.input', create = True)
    def test_withdraw_cash(self, mocked_input):
        mocked_input.side_effect = [100]
        result = withdraw_cash()
        self.assertEqual(result, 0)

    @mock.patch('ATM.input', create=True)
    def test_present_valid_interface(self, mocked_input):
        mocked_input.side_effect = [1, 100, 3]
        result = present_valid_interface()
        self.assertEqual(result, 0)

    @mock.patch('ATM.input', create=True)
    def test_present_invalid_interface(self, mocked_input):
        mocked_input.side_effect = [1333, 1222, 2222]
        result = present_invalid_interface(local_valid_pin=1234, attempt=3)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()