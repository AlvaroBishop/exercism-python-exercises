def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    aliquot_sum = 0
    for n in getFactors(number):
        aliquot_sum += n
    
    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum > number:
        return 'abundant'
    elif aliquot_sum < number:
        return 'deficient'
        

def getFactors(number):
    factors = []
    for n in range(1, number):
        if number % n == 0: 
            factors.append(n)
    return factors