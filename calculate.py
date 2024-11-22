import circle  # noqa: F401
import square  # noqa: F401
import triangle  # noqa: F401

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    "area-circle": 1,
    "perimeter-circle": 1,
    "area-square": 1,
    "perimeter-square": 1,
    "area-triangle": 3,
    "perimeter-triangle": 3
}


def calc(fig, func, size):
    assert fig in figs, f"Error figure: {fig}. Acceptable figures: {figs}."
    assert func in funcs, "Error function: {func}. Acceptable figures \
        {funcs}."
    assert len(size) == sizes.get(f"{func}-{fig}", 1), \
        f"Error number of parameters for {func} of {fig}."
    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes"
                                   "separated by space.\n").split(' ')))

    calc(fig, func, size)