from lexer import Lexer
from parser_ import Parser

while True:
    text = input("calc > ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    token_list = list(tokens)
    parser = Parser(token_list)
    tree = parser.parse()
    print(token_list)
    print(tree)

