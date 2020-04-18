from src.nodes import *
from src.tokens import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def advance(self):
        """Iterative function."""
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def raise_error(self):
        raise Exception("Invalid syntax")

    def parse(self):
        """The main function of the parser."""
        if self.current_token is None:
            return None

        result = self.expr()

        if self.current_token is not None:
            self.raise_error()

        return result

    def expr(self):
        """Expression- addition and subtraction functions, the highest level of hierarchy."""
        result = self.term()

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        """Terms - Multiplication and division functions, lower hierarchy level."""
        result = self.expon()

        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.expon())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.expon())

        return result

    def expon(self):  
        """Exponentiation - power function, lower hierarchy level."""
        result = self.factor()

        while self.current_token is not None and self.current_token.type == TokenType.POWER:
            if self.current_token.type == TokenType.POWER:
                self.advance()
                result = PowerNode(result, self.factor())

        return result

    def factor(self):
        """Other functions, lowest hierarchy level."""
        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()

            self.advance()
            return result

        if token.type == TokenType.LBRACKET:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RBRACKET:
                self.raise_error()

            self.advance()
            return result

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        elif token.type == TokenType.LETTER:
            self.advance()
            return LetterNode(token.value)

        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())

        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())

        elif token.type == TokenType.SIN:
            self.advance()
            return SinusNode(self.factor())

        elif token.type == TokenType.COS:
            self.advance()
            return CosinusNode(self.factor())

        elif token.type == TokenType.EXP:
            self.advance()
            return ExponentNode(self.factor())

        elif token.type == TokenType.SQRT:
            self.advance()
            return SquareNode(self.factor())

        self.raise_error()
