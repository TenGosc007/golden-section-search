class Config:
    X_POS = 100
    Y_POS = 100
    APP_WIDTH = 1080
    APP_HEIGHT = 720
    TEMPLATE_FUNCTIONS = [
        'x1^4 + x2^4 - 0.62x1^2 - 0.62x2^2',  # funkcja z czterema minimami lokalnymi
        '100(x2-x1^2)^2 + (1 - x1)^2',  # funkcja Rosenbrock'a
        '(x1 - x2 + x3)^2 + (-x1 + x2 + x3)^2 + (x1 + x2 - x3)^2',  # funkcja Zangwill'a
        '[1 + (x1 + x2 + 1)^2 * (19 - 14x1 + 3x1^2 - 14x2 + 6x1x2 + 3x2^2)] * [30 + (2x1 - 3x2)^2 * (18 - 32x1 + 12x1^2 +48x2 -36x1 * x2 + 27x2^2)]',  # funkcja Goldsteina-Prince'a z czterema minimami lokalnymi
        '(x1^2 + x2 - 11)^2 + (x1 + x2^2 -7)^2 - 200',  # zmodyfikowana funkcja Himmelblau'a
        '-20exp(-0.2 * sqrt(1/2(x1^2 + x2^2) - exp(1/2(cos(2 * 3.14 * x1) + cos(2 * 3.14 * x2))',  # funkcja Ackley'a dla n = 2
        '[x1^2 - cos(18x1)] + [x2^2 - cos(18x2)]',   # funkcja Rastrigina dla n = 2
        '[x1^2 - cos(18x1)] + [x2^2 - cos(18x2)] + [x3^2 - cos(18x3)]',   # funkcja Rastrigina dla n = 3
        '4x1^2 - 2.1x1^4 + (x1^6) / 3 + x1x2 - 4x2^2 + 4x2^4',  # funkcja testowa Geem'a
        'sin(x1) * sin(x2) * exp(-(x1^2 + x2^2))',
        'x1 * exp(-(x1^2 + x2^2))',
    ]
