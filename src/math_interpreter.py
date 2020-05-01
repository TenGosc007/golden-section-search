from src.interpreter import Interpreter
from src.lexer import Lexer
from src.math_parser import Parser


class MathInterpreter:
    def __init__(self, function):
        self.function = function
        self.token_list = self.get_token_list()

    @staticmethod
    def var_value(vars_value):
        """Function returns list of variables with values."""
        dict_comp = {f'x{i + 1}': vars_value[i] for i in range(len(vars_value))}
        return dict_comp

    def get_token_list(self):
        """Function create tokens."""
        lexer = Lexer(self.function)
        tokens = lexer.generate_tokens()
        token_list = list(tokens)
        return token_list

    def get_variables(self):
        """Function returns an array of variables that appeared in the equation."""
        lexer = Lexer(self.function)
        variables = lexer.find_variable(self.token_list)
        return variables

    def variables_amount(self):
        """Function returns number of variables in equation."""
        var_list = self.get_variables()
        return len(var_list)

    def calculate(self, vars_value):
        """Function returns the result of the equation."""
        variable = self.var_value(vars_value)
        parser = Parser(self.token_list, variable)
        tree = parser.parse()

        interpreter = Interpreter()
        value = interpreter.visit(tree)
        return value
