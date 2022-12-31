def steps(number):
    step = 0
    
    if number < 1:
        raise ValueError("Only positive integers are allowed")
        return step
    while(number != 1):
        step += 1
        number = (number / 2 if number % 2 == 0 else number * 3 + 1)
    return step
