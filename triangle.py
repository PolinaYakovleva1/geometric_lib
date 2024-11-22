def area(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        return (a + b + c) / 2
    else:
        raise ValueError("Error. The size must be greater than zero.")


def perimeter(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        return a + b + c
    else:
        raise ValueError("Error. The size must be greater than zero.")