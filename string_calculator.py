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

        # Check for negative numbers
        negatives = [num for num in num_list if num.strip().startswith("-") and num.strip()[1:].isdigit()]
        if negatives:
            raise InvalidInputException(f"Negative numbers not allowed: {', '.join(negatives)}")

        # Check for alphabetic characters after splitting
        if any(any(char.isalpha() for char in num) for num in num_list):
            raise InvalidInputException("Invalid inputs: Charaters are not allowed")

        # Filter out empty strings and convert valid numbers to integers
        valid_numbers = [int(num) for num in num_list if num.strip().isdigit()]
        return sum(valid_numbers)
