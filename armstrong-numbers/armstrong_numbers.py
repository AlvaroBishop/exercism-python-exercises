def is_armstrong_number(number):
    numbers = str(number)
    return sum(int(n) ** len(numbers) for n in numbers) == number
