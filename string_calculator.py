import re

class InvalidInputException(Exception):
    """Custom exception for invalid inputs."""
    pass

class StringCalculator:
    @staticmethod
    def add(numbers):
        if numbers is None:  # None input
            return 0
        if numbers == "":  # Empty string
            return 0

        # Handle custom delimiter
        delimiter = ","
        raw_delimiter = delimiter  # Default raw delimiter is ","
        if numbers.startswith("//"):
            # Extract custom delimiter
            delimiter_section = numbers[2:numbers.index("\n")]
            numbers = numbers[numbers.index("\n") + 1:]  # Remove the custom delimiter line
            # Handle single-character delimiters
            raw_delimiter = delimiter_section  # Use raw delimiter for replacement
            delimiter = re.escape(delimiter_section)  # Use escaped delimiter for regex

        # Replace new lines with the raw delimiter
        numbers = numbers.replace("\n", raw_delimiter)

        # Split numbers using the escaped delimiter
        num_list = re.split(delimiter, numbers)

        # Check for alphabetic characters after splitting
        if any(any(char.isalpha() for char in num) for num in num_list):
            raise InvalidInputException("Invalid inputs: Charaters are not allowed")

        print("numbers", numbers)  # Debugging output
        print("num_list", num_list)  # Debugging output

        # Filter out empty strings and convert valid numbers to integers
        valid_numbers = [int(num) for num in num_list if num.strip().isdigit()]
        return sum(valid_numbers)
