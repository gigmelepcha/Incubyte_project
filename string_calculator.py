class InvalidInputException(Exception):
    """Custom exception for invalid inputs."""
    pass

class StringCalculator:
    @staticmethod
    def parseString(numbers):
        """
        Parses the input string into a list of numbers based on the delimiter.

        Parameters:
        - numbers (str): The input string containing numbers.

        Returns:
        - list: A list of parsed numbers as strings.
        """
        if numbers is None or numbers =="":  # None input
            return 0
        # if numbers == "":  # Empty string
        #     return 0

        # Handle custom delimiter
        delimiter = ","
        raw_delimiter = delimiter  # Default raw delimiter is ","
        if numbers.startswith("//"):
            # Extract custom delimiter
            delimiter_section = numbers[2:numbers.index("\n")]
            numbers = numbers[numbers.index("\n") + 1:]  # Remove the custom delimiter line
            raw_delimiter = delimiter_section  # Use raw delimiter for replacement

        # Replace new lines with the raw delimiter
        numbers = numbers.replace("\n", raw_delimiter)

        # Manually split the string while preserving negative numbers
        num_list = []
        current_number = ""
        for i, char in enumerate(numbers):
            # Check if the character is the delimiter and not part of a negative number
            if char == raw_delimiter and (i == 0 or numbers[i - 1] != "-"):
                num_list.append(current_number)
                current_number = ""
            else:
                current_number += char
        if current_number:  # Add the last number
            num_list.append(current_number)
        return num_list
    @staticmethod
    def HandleNegative(num_list):
        # Check for negative numbers
        negatives = [num for num in num_list if num.strip().startswith("-") and num.strip()[1:].isdigit()]
        if negatives:
            raise InvalidInputException(f"Negative numbers not allowed: {', '.join(negatives)}")
        # Check for invalid characters (alphabetic or non-numeric)
        if any(any(not char.isdigit() for char in num.strip()) for num in num_list):
            raise InvalidInputException("Invalid inputs: Characters or non-numeric values are not allowed")    # Filter out empty strings and convert valid numbers to integers
     
    @staticmethod
    def add(numbers):
        """
        Adds numbers provided in a string format, supporting custom delimiters and validations.

        Parameters:
        - numbers (str): A string containing numbers separated by delimiters.

        Returns:
        - int: The sum of the numbers in the string.

        Raises:
        - InvalidInputException: If the input contains invalid characters, non-numeric values, or negative numbers.

        """
        num_list = StringCalculator.parseString(numbers)
        if num_list == 0:
            return 0
        StringCalculator.HandleNegative(num_list)
        valid_numbers = [int(num) for num in num_list if num.strip().isdigit()]
        return sum(valid_numbers)
