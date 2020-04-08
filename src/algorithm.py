from math import sqrt


class Algorithm:
    def __init__(self, a, b, n):
        self.epsilon = 0.001
        self.k = (sqrt(5) - 1) / 2
        self.n = n
        self.vars_dict = self.get_vars_dict(a, b, self.n)
        self.iteration = 0

    def get_vars_dict(self, a, b, n):
        vars_dict = {}
        for i in range(n):
            vars_dict['a_' + str(i)] = a[i]
            vars_dict['b_' + str(i)] = b[i]
            vars_dict['x1_' + str(i)] = a[i] + (1 - self.k) * (b[i] - a[i])
            vars_dict['x2_' + str(i)] = a[i] + self.k * (b[i] - a[i])

        return vars_dict

    def find_minimum_value(self):
        x_min = 0
        while sqrt(pow(self.vars_dict['b_0'] - self.vars_dict['a_0'], 2)) > self.epsilon:
            fx1 = self.example_function_n1(self.vars_dict['x1_0'])
            fx2 = self.example_function_n1(self.vars_dict['x2_0'])
            self.iteration += 1
            print('Iteracja: ', self.iteration)
            min1 = min([fx1, fx2])

            if min1 == fx1:
                self.vars_dict['b_0'] = self.vars_dict['x2_0']
                self.vars_dict['x2_0'] = self.vars_dict['x1_0']
                self.vars_dict['x1_0'] = self.vars_dict['b_0'] - self.k * (
                        self.vars_dict['b_0'] - self.vars_dict['a_0'])
            else:
                self.vars_dict['a_0'] = self.vars_dict['x1_0']
                self.vars_dict['x1_0'] = self.vars_dict['x2_0']
                self.vars_dict['x2_0'] = self.vars_dict['a_0'] + self.k * (
                        self.vars_dict['b_0'] - self.vars_dict['a_0'])

            x_min = (self.vars_dict['a_0'] + self.vars_dict['b_0']) / 2
            print('a: ', self.vars_dict['a_0'], end='\t')
            print('x1: ', self.vars_dict['x1_0'], end='\t')
            print('x2: ', self.vars_dict['x2_0'], end='\t')
            print('b: ', self.vars_dict['b_0'])
            print(x_min, end='\n\n')

        return x_min

    @staticmethod
    def example_function_n1(x):
        """Function has got minimum at x = 0.5."""
        return pow(x - 0.5, 2) + 0.5

    @staticmethod
    def example_function_n2(x, y):
        """Function has got minimum at x = 0.5 and y = 0.5."""
        return pow(x - 0.5, 4) + pow(y - 0.5, 4) + 2 * pow(x - 0.5, 2) + pow(y - 0.5, 2) + 4 * (x - 0.5) * (y - 0.5)


if __name__ == '__main__':
    alg = Algorithm([0], [1], 1)
    print('Szukany punkt:', alg.find_minimum_value())
