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
        x_min = 0
        while sqrt(pow(self.vars_dict['b_0'] - self.vars_dict['a_0'], 2)) > self.epsilon:
            fx1 = self.example_function_n1(self.vars_dict['x1_0'])
            fx2 = self.example_function_n1(self.vars_dict['x2_0'])
            self.iteration += 1
            print('Iteracja: ', self.iteration)
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
            print('a: ', self.vars_dict['a_0'], end='\t')
            print('x1: ', self.vars_dict['x1_0'], end='\t')
            print('x2: ', self.vars_dict['x2_0'], end='\t')
            print('b: ', self.vars_dict['b_0'])
            print(x_min, end='\n\n')

        return x_min

    def find_minimum_value_n2(self):
        x1_min = 0
        x2_min = 0
        while sqrt(pow(self.vars_dict['b_0'] - self.vars_dict['a_0'], 2) + pow(
                self.vars_dict['b_1'] - self.vars_dict['a_1'], 2)) > self.epsilon:

            self.iteration += 1
            print('Iteracja: ', self.iteration)

            f_pt1 = self.example_function_n2(self.vars_dict['x1_0'], self.vars_dict['x1_1'])
            f_pt2 = self.example_function_n2(self.vars_dict['x1_0'], self.vars_dict['x2_1'])
            f_pt3 = self.example_function_n2(self.vars_dict['x2_0'], self.vars_dict['x1_1'])
            f_pt4 = self.example_function_n2(self.vars_dict['x2_0'], self.vars_dict['x2_1'])

            minimum = min([f_pt1, f_pt2, f_pt3, f_pt4])
            if minimum == f_pt1:
                self.vars_dict['b_0'] = self.vars_dict['x2_0']
                self.vars_dict['b_1'] = self.vars_dict['x2_1']
                print('x1, x2', self.vars_dict['x1_0'], self.vars_dict['x1_1'])
                print('f(x1, x2) = ', f_pt1)
            elif minimum == f_pt2:
                self.vars_dict['b_0'] = self.vars_dict['x2_0']
                self.vars_dict['a_1'] = self.vars_dict['x1_1']
                print('x1, x2', self.vars_dict['x1_0'], self.vars_dict['x2_1'])
                print('f(x1, x2) = ', f_pt2)
            elif minimum == f_pt3:
                self.vars_dict['a_0'] = self.vars_dict['x1_0']
                self.vars_dict['a_1'] = self.vars_dict['x1_1']
                print('x1, x2', self.vars_dict['x2_0'], self.vars_dict['x1_1'])
                print('f(x1, x2) = ', f_pt3)
            else:
                self.vars_dict['a_0'] = self.vars_dict['x1_0']
                self.vars_dict['b_1'] = self.vars_dict['x2_1']
                print('x1, x2', self.vars_dict['x2_0'], self.vars_dict['x2_1'])
                print('f(x1, x2) = ', f_pt4)

            self.vars_dict['x1_0'] = self.vars_dict['a_0'] + (1 - self.k) * (
                    self.vars_dict['b_0'] - self.vars_dict['a_0'])
            self.vars_dict['x2_0'] = self.vars_dict['a_0'] + self.k * (self.vars_dict['b_0'] - self.vars_dict['a_0'])

            self.vars_dict['x1_1'] = self.vars_dict['a_1'] + (1 - self.k) * (
                    self.vars_dict['b_1'] - self.vars_dict['a_1'])
            self.vars_dict['x2_1'] = self.vars_dict['a_1'] + self.k * (self.vars_dict['b_1'] - self.vars_dict['a_1'])

        return x1_min, x2_min

    def find_minimum_test(self):
        a1 = 0  # lower bound for variable x
        b1 = 1  # upper bound for variable x
        a2 = 0  # lower bound for variable y
        b2 = 1  # upper bound for variable y
        epsilon = 0.00000001  # termination criteria
        tau = (sqrt(5) - 1) / 2  # golden number
        k = 0  # number of iterations

        x1 = a1 + (1 - tau) * (b1 - a1)
        x2 = a1 + tau * (b1 - a1)
        y1 = a2 + (1 - tau) * (b2 - a2)
        y2 = a2 + tau * (b2 - a2)

        ek = [x1, y1]  # Point A
        fk = [x1, y2]  # Point C
        hk = [x2, y1]  # Point B
        gk = [x2, y2]  # Point D
        fek = self.example_function_n2(x1, y1)
        ffk = self.example_function_n2(x1, y2)
        fhk = self.example_function_n2(x2, y1)
        fgk = self.example_function_n2(x2, y2)  # function values at points A, B, C and D.

        min1 = None
        while sqrt(pow((b1 - a1), 2) + pow((b2 - a2), 2)) > epsilon:  # termination condition
            k = k + 1
            min1 = min([fek, fhk, ffk, fgk])

            if min1 == fek:
                b1 = x2
                b2 = y2
            elif min1 == ffk:
                b1 = x2
                a2 = y1
            elif min1 == fgk:
                a1 = x1
                a2 = y1
            elif min1 == fhk:
                a1 = x1
                b2 = y2

            x1 = a1 + (1 - tau) * (b1 - a1)
            x2 = a1 + tau * (b1 - a1)
            y1 = a2 + (1 - tau) * (b2 - a2)
            y2 = a2 + tau * (b2 - a2)
            fek = self.example_function_n2(x1, y1)
            ffk = self.example_function_n2(x1, y2)
            fhk = self.example_function_n2(x2, y1)
            fgk = self.example_function_n2(x2, y2)
            min1 = min([fek, fhk, ffk, fgk])

        if min1 == fek:
            print(f'minimum at the point ({x1},{y1})')
        elif min1 == ffk:
            print(f'minimum at the point ({x1},{y2})')
        elif min1 == fhk:
            print(f'minimum at the point ({x2},{y1}))')
        elif min1 == fgk:
            print(f'minimum at the point ({x2},{y2})')

        print(f'minimum value {min1}')
        print(f'number of iterations {k}')

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
    # print('Szukany punkt:', alg.find_minimum_value_n1())
    # print('Szukany punkt:', alg.find_minimum_value_n2())
    alg.find_minimum_matlab()
