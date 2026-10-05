def equilateral(sides):
    a, b, c = sides
    if is_triangle(a, b, c):
        return a == b == c
    return False

def isosceles(sides):
    a, b, c = sides
    if is_triangle(a, b ,c):
        return a == b or b == c or c == a
    return False

def scalene(sides):
    a, b, c = sides
    if is_triangle(a, b, c):
        return a != b and b != c and a != c
    return False

def is_triangle(a , b ,c):
    if (a > 0 and b > 0 and c > 0) and (a + b >= c and b + c >= a and a + c >= b):
        return True
    return False
