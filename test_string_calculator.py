import unittest
from string_calculator import StringCalculator
from string_calculator import InvalidInputException

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

    def test_none_input(self):
        self.assertEqual(StringCalculator.add(None), 0)

    def test_invalid_inputs(self):
        # Test input with alphabets
        with self.assertRaises(InvalidInputException) as context:
            StringCalculator.add("1,a,3")
        self.assertEqual(str(context.exception), "Invalid inputs: Charaters are not allowed")

        # Test input with mixed alphabets and numbers
        with self.assertRaises(InvalidInputException) as context:
            StringCalculator.add("1asd")
        self.assertEqual(str(context.exception), "Invalid inputs: Charaters are not allowed")

        # Test input with only alphabets
        with self.assertRaises(InvalidInputException) as context:
            StringCalculator.add("abc")
        self.assertEqual(str(context.exception), "Invalid inputs: Charaters are not allowed")

    def test_new_line_delimiters(self):
        # Test with new lines between numbers
        self.assertEqual(StringCalculator.add("1\n2,3"), 6)
        self.assertEqual(StringCalculator.add("10\n20\n30"), 60)
        self.assertEqual(StringCalculator.add("\n9,1"), 10)
        self.assertEqual(StringCalculator.add("1,\n3"), 4)

    def test_invalid_inputs_with_new_lines(self):
        # Test invalid input with alphabets and new lines
        with self.assertRaises(InvalidInputException):
            StringCalculator.add("1\n2,a")
    
    def test_single_character_delimiter(self):
        # Test with a single-character custom delimiter
        self.assertEqual(StringCalculator.add("//;\n1;2"), 3)  # Delimiter is ";"
        self.assertEqual(StringCalculator.add("//|\n10|20|30"), 60)  # Delimiter is "|"
        self.assertEqual(StringCalculator.add("//#\n4#5#6"), 15)  # Delimiter is "#"

    def test_single_character_delimiter_with_new_lines(self):
        # Test with a single-character custom delimiter and new lines
        self.assertEqual(StringCalculator.add("//;\n1\n2;3"), 6)  # Mixed ";" and "\n"
        self.assertEqual(StringCalculator.add("//|\n10|20\n30"), 60)  # Mixed "|" and "\n"

    def test_invalid_inputs_with_single_character_delimiter(self):
        # Test invalid inputs with a single-character custom delimiter
        with self.assertRaises(InvalidInputException):
            StringCalculator.add("//;\n1;a;3")  # Contains alphabetic character "a"
        with self.assertRaises(InvalidInputException):
            StringCalculator.add("//|\n10|20|abc")  # Contains alphabetic characters "abc"

    def test_negative_numbers(self):
        # Test with a single negative number
        with self.assertRaises(InvalidInputException) as context:
            StringCalculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

        # Test with multiple negative numbers
        with self.assertRaises(InvalidInputException) as context:
            StringCalculator.add("1,-2,-3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -3")

        # Test with custom delimiter and negative numbers
        with self.assertRaises(InvalidInputException) as context:
            StringCalculator.add("//;\n1;-2;3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

        # Test with custom delimiter "-" and negative numbers
        with self.assertRaises(InvalidInputException) as context:
            StringCalculator.add("//-\n1--2")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

if __name__ == '__main__':
    unittest.main()
