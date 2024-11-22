def area(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c))**0.5
    else:
        raise ValueError("Error. The size must be greater than zero.")


def perimeter(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        return a + b + c
    else:
        raise ValueError("Error. The size must be greater than zero.")