import math


def area(r):
    if r >= 0:
        return math.pi * r * r
    else:
        raise ValueError("Error. The radius is less than 0.")


def perimeter(r):
    if r >= 0:
        return 2 * math.pi * r
    else:
        raise ValueError("Error. The radius is less than 0.")