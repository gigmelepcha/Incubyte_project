class StringCalculator:
    @staticmethod
    def add(numbers):
        if numbers == "":
            return 0
        elif "," not in numbers:  # single number
            return int(numbers)
        else:
            num_list = numbers.split(",") # multiple numbers seperated by comma
            return sum(int(num) for num in num_list)
