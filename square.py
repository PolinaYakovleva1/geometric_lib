def area(a):
    if a >= 0:
        return a * a
    else:
        raise ValueError("Size should be > 0.")


def perimeter(a):
    if a >= 0:
        return 4 * a
    else:
        raise ValueError("Size should be > 0.")
