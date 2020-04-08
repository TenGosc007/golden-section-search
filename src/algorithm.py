from math import sqrt


class Algorithm:
    def __init__(self, a, b):
        self.epsilon = 0.001
        self.k = (sqrt(5) - 1) / 2
        self.a = a
        self.b = b
        self.x1 = a + (1 - self.k) * (self.b - self.a)
        self.x2 = a + self.k * (self.b - self.a)
        self.iteration = 0

    def find_minimum_value(self):
        x_min = 0
        while sqrt(pow(self.b - self.a, 2)) > self.epsilon:
            fx1 = self.example_function(self.x1)
            fx2 = self.example_function(self.x2)
            self.iteration += 1
            print('Iteracja: ', self.iteration)
            min1 = min([fx1, fx2])

            if min1 == fx1:
                self.b = self.x2
                self.x2 = self.x1
                self.x1 = self.b - self.k * (self.b - self.a)
            else:
                self.a = self.x1
                self.x1 = self.x2
                self.x2 = self.a + self.k * (self.b - self.a)

            x_min = (self.a + self.b) / 2
            print('a: ', self.a, end='\t')
            print('x1: ', self.x1, end='\t')
            print('x2: ', self.x2, end='\t')
            print('b: ', self.b)
            print(x_min, end='\n\n')

        return x_min

    @staticmethod
    def example_function(x):
        return pow(x - 0.5, 2) + 0.5


if __name__ == '__main__':
    alg = Algorithm(0, 1)
    print('Szukany punkt:', alg.find_minimum_value())
