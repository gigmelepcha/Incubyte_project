class InvalidInputException(Exception):
    """Custom exception for invalid inputs."""
    pass

class StringCalculator:
    @staticmethod
    def add(numbers):
        if numbers is None: # None input
            return 0
        if numbers == "": # Empty string
            return 0
        elif "," not in numbers:    # Single number
            if not numbers.isdigit():  # Check for alphabetic characters
                raise InvalidInputException("Invalid inputs: Charaters are not allowed")
            return int(numbers)
        else:
            num_list = numbers.split(",") # multiple numbers seperated by comma
            # Check for alphabetic characters after splitting
            if any(any(char.isalpha() for char in num) for num in num_list):
                raise InvalidInputException("Invalid inputs: Charaters are not allowed")
            return sum(int(num) for num in num_list)
