import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(StringCalculator.add(''), 0)
    def test_single_number(self):
        self.assertEqual(StringCalculator.add('1'), 1)
        self.assertEqual(StringCalculator.add('5'), 5)

    def test_two_numbers(self):
        self.assertEqual(StringCalculator.add('1,2'), 3)
        self.assertEqual(StringCalculator.add('10,20'), 30)

    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator.add('1,2,3'), 6)
        self.assertEqual(StringCalculator.add('10,20,30,40'), 100)


if __name__ == '__main__':
    unittest.main()
