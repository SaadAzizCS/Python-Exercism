def equilateral(sides):
    side1, side2, side3 = sides
    if is_triangle(side1, side2, side3):
        return side1 == side2 == side3
    return False

def isosceles(sides):
    side1, side2, side3 = sides
    if is_triangle(side1, side2 ,side3):
        return side1 == side2 or side2 == side3 or side3 == side1
    return False

def scalene(sides):
    side1, side2, side3 = sides
    if is_triangle(side1, side2, side3):
        return side1 != side2 and side2 != side3 and side1 != side3
    return False

def is_triangle(side1 , side2 ,side3):
    if (side1 > 0 and side2 > 0 and side3 > 0) and (side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2):
        return True
    return False
