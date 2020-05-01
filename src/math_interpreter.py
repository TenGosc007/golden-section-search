from src.interpreter import Interpreter
from src.lexer import Lexer
from src.math_parser import Parser


def var_value(vars_list):
    """Function returns list of variables with values."""
    dict_comp = {f'x{i}': vars_list[i] for i in range(len(vars_list))}
    return dict_comp


def function_lexer(function):
    """Function create tokens."""
    lexer = Lexer(function)
    tokens = lexer.generate_tokens()
    token_list = list(tokens)
    return token_list


def variables_amount(function, token_list):
    """Function returns an array of variables that appeared in the equation."""
    lexer = Lexer(function)
    variables = lexer.find_variable(token_list)
    return variables


def function_calculation(token_list, vars_list):
    """Function returns the result of the equation."""
    variable = var_value(vars_list)
    parser = Parser(token_list, variable)
    tree = parser.parse()

    interpreter = Interpreter()
    value = interpreter.visit(tree)
    return value
