import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(StringCalculator.add(''), 0)

if __name__ == '__main__':
    unittest.main()

    