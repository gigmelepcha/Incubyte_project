class InvalidInputException(Exception):
    """Custom exception for invalid inputs."""
    pass


class StringCalculator:
    @staticmethod
    def _parse_numbers(numbers, default_delimiter=","):
        """
        Parses the input string into a list of numbers based on the delimiter.

        Parameters:
        - numbers (str): The input string containing numbers.
        - default_delimiter (str): The default delimiter to use for splitting.

        Returns:
        - list: A list of parsed numbers as strings.
        """
        if not numbers:  # Handle None or empty string
            return []

        delimiter = default_delimiter

        # Handle custom delimiter
        if numbers.startswith("//"):
            delimiter_section = numbers[2:numbers.index("\n")]
            numbers = numbers[numbers.index("\n") + 1:]  # Remove the custom delimiter line
            delimiter = delimiter_section

        # Replace newlines with the delimiter
        numbers = numbers.replace("\n", delimiter)
        # Split numbers manually to handle edge cases
        num_list = []
        current_number = ""
        for i, char in enumerate(numbers):
            if char == delimiter and (i == 0 or numbers[i - 1] != "-"):  # Not part of a negative number
                num_list.append(current_number)
                current_number = ""
            else:
                current_number += char
        if current_number:  # Add the last number
            num_list.append(current_number)
        return num_list

    @staticmethod
    def _validate_numbers(num_list):
        """
        Validates the parsed numbers for negatives and invalid characters.

        Parameters:
        - num_list (list): A list of parsed numbers as strings.

        Raises:
        - InvalidInputException: If negative numbers or invalid characters are found.
        """
        # Check for negative numbers
        negatives = [num for num in num_list if num.strip().startswith("-") and num.strip()[1:].isdigit()]
        if negatives:
            raise InvalidInputException(f"Negative numbers not allowed: {', '.join(negatives)}")

        # Check for invalid characters (alphabetic or non-numeric)
        if any(any(not char.isdigit() for char in num.strip()) for num in num_list): 
            raise InvalidInputException("Invalid inputs: Characters or non-numeric values are not allowed")

    @staticmethod
    def checkOccurance(num_list):
        """
        Checks the occurrence of each number in the input string. If a number occurs
        three or more times, returns its cube once; otherwise, returns the number as it is.

        Parameters:
        - numbers (str): A string containing numbers separated by delimiters.

        Returns:
        - list: A list of numbers or their cubes based on the occurrence count.
        """
        if not num_list:
            return []
        occurrence_count = {}

        for num in num_list:
            occurrence_count[num] = occurrence_count.get(num, 0) + 1

        result = []
        processed = set()
        for num in num_list:
            if occurrence_count[num] >= 3 and num not in processed:
                result.append(str(int(num) ** 3))
                processed.add(num)
            elif occurrence_count[num] < 3 and num not in processed:
                result.append(num)
        return result

    @staticmethod
    def add(numbers):
        """
        Adds numbers provided in a string format, supporting custom delimiters and validations.

        Parameters:
        - numbers (str): A string containing numbers separated by delimiters.

        Returns:
        - int: The sum of the numbers in the string.
        """
        num_list = StringCalculator._parse_numbers(numbers)
        if not num_list:
            return 0

        StringCalculator._validate_numbers(num_list)
        num_list = StringCalculator.checkOccurance(num_list)
        return sum(int(num) for num in num_list if num.strip().isdigit())
