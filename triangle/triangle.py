def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) < 3

def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3
    
def is_triangle(sides):
    return sum(sides) > 0 and (sum(sides) >= max(sides) *2)