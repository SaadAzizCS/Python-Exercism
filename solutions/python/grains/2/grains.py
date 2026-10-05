"""
calculates number of grains on a chessboard
"""
def square(number):
    if 0 < number <= 64:
        return 2**(number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    return 2**64 - 1