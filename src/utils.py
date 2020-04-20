import re


def camel_to_snake_case(string):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    name = pattern.sub('_', string).lower()
    return name
