from math import sqrt


class Algorithm:
    def __init__(self, a, b):
        self.epsilon = 0.001
        self.k = (sqrt(5) - 1) / 2
        self.a = a
        self.b = b
