from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

# TEMPLATE_FUNCTIONS = [
#         'x1^4 + x2^4 - 0.62*x1^2 - 0.62*x2^2',  # funkcja z czterema minimami lokalnymi
#         '100*(x2-x1^2)^2 + (1 - x1)^2',  # funkcja Rosenbrock'a
#         '(x1 - x2 + x3)^2 + (-x1 + x2 + x3)^2 + (x1 + x2 - x3)^2',  # funkcja Zangwill'a
#         '(1 + (x1 + x2 + 1)^2 * (19 - 14*x1 + 3*x1^2 - 14*x2 + 6*x1*x2 + 3*x2^2)) * (30 + (2*x1 - 3*x2)^2 * (18 - 32*x1 + 12*x1^2 +48*x2 -36*x1 * x2 + 27*x2^2))',  # funkcja Goldsteina-Prince'a z czterema minimami lokalnymi
#         '(x1^2 + x2 - 11)^2 + (x1 + x2^2 -7)^2 - 200',  # zmodyfikowana funkcja Himmelblau'a
#         '-20*exp(-0.2 * sqrt(1/2*(x1^2 + x2^2))) - exp(1/2*(cos(2 * 3.14 * x1) + cos(2 * 3.14 * x2)))',  # funkcja Ackley'a dla n = 2
#         '(x1^2 - cos(18*x1)) + (x2^2 - cos(18*x2))',   # funkcja Rastrigina dla n = 2
#         '(x1^2 - cos(18*x1)) + (x2^2 - cos(18*x2)) + (x3^2 - cos(18*x3))',   # funkcja Rastrigina dla n = 3
#         '4*x1^2 - 2.1*x1^4 + (x1^6) / 3 + x1*x2 - 4*x2^2 + 4*x2^4',  # funkcja testowa Geem'a
#         'sin(x1) * sin(x2) * exp(-(x1^2 + x2^2))',
#         'x1 * exp(-(x1^2 + x2^2))',
#     ]

# for i in range(len(TEMPLATE_FUNCTIONS)):
#     text = TEMPLATE_FUNCTIONS[i]
#     # text = input("calc > ")
#     lexer = Lexer(text)
#     tokens = lexer.generate_tokens()
#     token_list = list(tokens)
#     parser = Parser(token_list)
#     tree = parser.parse()
#     print(token_list)
#     print(tree)
#     print('\n')

while True:
    try:
        text = input("calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        token_list = list(tokens)
        parser = Parser(token_list)
        tree = parser.parse()
        print(token_list)
        print(tree)
        
        if not tree: continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print("result > ", value)
    except Exception as e:
        print(e)
        break
        

