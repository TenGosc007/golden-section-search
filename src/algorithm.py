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

    def find_minimum_value_n1(self):
        x_min = None
        minimum = None

        while sqrt(pow(self.vars_dict['b_0'] - self.vars_dict['a_0'], 2)) > self.epsilon:
            fx1 = self.example_function_n1(self.vars_dict['x1_0'])
            fx2 = self.example_function_n1(self.vars_dict['x2_0'])
            self.iteration += 1
            minimum = min([fx1, fx2])

            if minimum == fx1:
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

        print(f'Minimum at the point {x_min}')
        print(f'Minimum value {minimum}')
        print(f'Number of iterations {self.iteration}')

    def find_minimum_value_n2(self):
        fek = self.example_function_n2(self.vars_dict['x1_0'], self.vars_dict['x1_1'])
        ffk = self.example_function_n2(self.vars_dict['x1_0'], self.vars_dict['x2_1'])
        fhk = self.example_function_n2(self.vars_dict['x2_0'], self.vars_dict['x1_1'])
        fgk = self.example_function_n2(self.vars_dict['x2_0'], self.vars_dict['x2_1'])

        minimum = None
        while sqrt(pow(self.vars_dict['b_0'] - self.vars_dict['a_0'], 2) + pow(
                self.vars_dict['b_1'] - self.vars_dict['a_1'], 2)) > self.epsilon:
            self.iteration += 1
            minimum = min([fek, fhk, ffk, fgk])

            if minimum == fek:
                self.vars_dict['b_0'] = self.vars_dict['x2_0']
                self.vars_dict['b_1'] = self.vars_dict['x2_1']
            elif minimum == ffk:
                self.vars_dict['b_0'] = self.vars_dict['x2_0']
                self.vars_dict['a_1'] = self.vars_dict['x1_1']
            elif minimum == fgk:
                self.vars_dict['a_0'] = self.vars_dict['x1_0']
                self.vars_dict['a_1'] = self.vars_dict['x1_1']
            elif minimum == fhk:
                self.vars_dict['a_0'] = self.vars_dict['x1_0']
                self.vars_dict['b_1'] = self.vars_dict['x2_1']

            self.vars_dict['x1_0'] = self.vars_dict['a_0'] + (1 - self.k) * (
                    self.vars_dict['b_0'] - self.vars_dict['a_0'])
            self.vars_dict['x2_0'] = self.vars_dict['a_0'] + self.k * (self.vars_dict['b_0'] - self.vars_dict['a_0'])
            self.vars_dict['x1_1'] = self.vars_dict['a_1'] + (1 - self.k) * (
                    self.vars_dict['b_1'] - self.vars_dict['a_1'])
            self.vars_dict['x2_1'] = self.vars_dict['a_1'] + self.k * (self.vars_dict['b_1'] - self.vars_dict['a_1'])

            fek = self.example_function_n2(self.vars_dict['x1_0'], self.vars_dict['x1_1'])
            ffk = self.example_function_n2(self.vars_dict['x1_0'], self.vars_dict['x2_1'])
            fhk = self.example_function_n2(self.vars_dict['x2_0'], self.vars_dict['x1_1'])
            fgk = self.example_function_n2(self.vars_dict['x2_0'], self.vars_dict['x2_1'])

            minimum = min([fek, fhk, ffk, fgk])

        x1_0 = self.vars_dict['x1_0']
        x2_0 = self.vars_dict['x2_0']
        x1_1 = self.vars_dict['x1_1']
        x2_1 = self.vars_dict['x2_1']

        if minimum == fek:
            print(f'Minimum at the point: ({x1_0},{x1_1})')
        elif minimum == ffk:
            print(f'Minimum at the point: ({x1_0},{x2_1})')
        elif minimum == fhk:
            print(f'Minimum at the point: ({x2_0},{x1_1}))')
        elif minimum == fgk:
            print(f'Minimum at the point: ({x2_0},{x2_1})')

        print(f'Minimum value: {minimum}')
        print(f'Number of iterations: {self.iteration}')

    @staticmethod
    def example_function_n1(x):
        """Function has got minimum at x = 0.5."""
        return pow(x - 0.5, 2) + 0.5

    @staticmethod
    def example_function_n2(x, y):
        """Function has got minimum at x = 0.5 and y = 0.5."""
        return pow(x - 0.5, 4) + pow(y - 0.5, 4) + 2 * pow(x - 0.5, 2) + 2 * pow(y - 0.5, 2) + 4 * (x - 0.5) * (y - 0.5)


if __name__ == '__main__':
    alg = Algorithm([0, 0], [1, 1], 2)
    # alg.find_minimum_value_n1()
    alg.find_minimum_value_n2()
