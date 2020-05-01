from src.tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'
LETTERS = 'abcxyz'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        """Iterative function."""
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        """Function creates tokens for each expression."""
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.current_char == '[':
                self.advance()
                yield Token(TokenType.LBRACKET)
            elif self.current_char == ']':
                self.advance()
                yield Token(TokenType.RBRACKET)
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.POWER)

            elif self.current_char == 's':
                self.advance()
                if self.current_char == 'i':
                    self.advance()
                    if self.current_char == 'n':
                        self.advance()
                        yield Token(TokenType.SIN)
                elif self.current_char == 'q':
                    self.advance()
                    if self.current_char == 'r':
                        self.advance()
                        if self.current_char == 't':
                            self.advance()
                            yield Token(TokenType.SQRT)

            elif self.current_char == 'c':
                prev = self.current_char
                self.advance()
                if self.current_char == 'o':
                    self.advance()
                    if self.current_char == 's':
                        self.advance()
                        yield Token(TokenType.COS)
                else:
                    while self.current_char is not None and self.current_char in DIGITS:
                        prev += self.current_char
                        self.advance()
                    yield Token(TokenType.LETTER, prev)

            elif self.current_char == 'e':
                self.advance()
                if self.current_char == 'x':
                    self.advance()
                    if self.current_char == 'p':
                        self.advance()
                        yield Token(TokenType.EXP)

            elif self.current_char in LETTERS:
                yield self.generate_letter()
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        """Function create nubmer token and supports dot expression."""
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))

    def generate_letter(self):
        """Function create nubmer token and supports index expression."""
        letter = self.current_char
        self.advance()

        while self.current_char is not None and self.current_char in DIGITS:
            letter += self.current_char
            self.advance()

        return Token(TokenType.LETTER, letter)

    def find_variable(self, tokens):
        variables = []
        for i in range(len(tokens)):
            if (tokens[i]).type == TokenType.LETTER and (tokens[i]).value not in variables:
                variables.append((tokens[i]).value)

        return variables
