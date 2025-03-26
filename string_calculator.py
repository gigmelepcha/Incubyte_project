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

        # Replace new lines with commas
        numbers = numbers.replace("\n", ",")

        # Handle single number
        if "," not in numbers:
            if not numbers.isdigit():  # Check for alphabetic characters
                raise InvalidInputException("Invalid inputs: Characters are not allowed")
            return int(numbers)

        # Handle multiple numbers
        num_list = numbers.split(",")  # Split by commas
        # Check for alphabetic characters after splitting
        if any(any(char.isalpha() for char in num) for num in num_list):
            raise InvalidInputException("Invalid inputs: Characters are not allowed")

        # Filter out empty strings and convert valid numbers to integers
        valid_numbers = [int(num) for num in num_list if num.strip().isdigit()]
        return sum(valid_numbers)
