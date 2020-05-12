import math
import re


def camel_to_snake_case(string):
    """Change CamelCase string to snake_case."""
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    name = pattern.sub('_', string).lower()
    return name


def example_function_n1(variables):
    """Function has got minimum at (0)."""
    return pow(variables, 2)


def example_function_n2(variables):
    """Function has got minimum at (0, 0)."""
    return pow(variables[0], 2) + pow(variables[1], 2)


def example_function_n3(variables):
    """Function has got minimum at (0, 0, 0)."""
    return pow(variables[0], 2) + pow(variables[1], 2) + pow(variables[2], 2)


def example_function_n4(variables):
    """Function has got minimum at (0, 0, 0, 0)."""
    return pow(variables[0], 2) + pow(variables[1], 2) + pow(variables[2], 2) + pow(variables[3], 2)


def example_function_n5(variables):
    """Function has got minimum at (0, 0, 0, 0, 0)."""
    return pow(variables[0], 2) + pow(variables[1], 2) + pow(variables[2], 2) + pow(variables[3], 2) + pow(
        variables[4], 2)


def get_range():
    x0 = 0
    d = 5

    krok = 0.01 * math.sqrt(d)
    j = 0
    f = example_function_n1
    y0 = f(x0)
    while j < 2:
        x = x0 + krok * d
        y = f(x)
        if y0 <= y:
            krok = -krok
            j += 1
        else:
            while y0 > y:
                krok = 2 * krok
                y0 = y
                x = x + krok * d
                y = f(x)
            j = 1
            break
    x2 = x
    x1 = x0 + krok * (j - 1) * d
    a = d * (x1 - x0) / d
    b = d * (x2 - x0) / d

    print(a, x1, x2, b)


if __name__ == '__main__':
    get_range()
