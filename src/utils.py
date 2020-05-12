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
