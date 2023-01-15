import math
def score(x, y):
    r = math.sqrt(x**2 + y**2)
    return (r <= 10) * 1 + (r <= 5) *  4 + (r <= 1) * 5