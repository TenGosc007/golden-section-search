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
            vars_dict[f'a_{i}'] = a[i]
            vars_dict[f'b_{i}'] = b[i]
            vars_dict[f'x1_{i}'] = a[i] + (1 - self.k) * (b[i] - a[i])
            vars_dict[f'x2_{i}'] = a[i] + self.k * (b[i] - a[i])

        return vars_dict

    def find_minimum_value_n1(self):
        combinations = self.create_var_combinations(self.n)
        x_min = None
        minimum = None

        while self.count_distance() > self.epsilon:
            points = [self.vars_dict[x[0]] for x in combinations]
            f_value = [self.example_function_n1(points[i]) for i in range(len(points))]
            minimum = min(f_value)
            self.iteration += 1

            if minimum == f_value[0]:
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
        combinations = self.create_var_combinations(self.n)
        points = [(self.vars_dict[x], self.vars_dict[y]) for x, y in combinations]
        f_value = [self.example_function_n2(points[i]) for i in range(len(points))]
        minimum = min(f_value)

        while self.count_distance() > self.epsilon:
            self.iteration += 1
            self.calculate_a_b_value(f_value, minimum, combinations)
            self.calculate_x1_x2_value()

            points = [(self.vars_dict[x], self.vars_dict[y]) for x, y in combinations]
            f_value = [self.example_function_n2(points[i]) for i in range(len(points))]
            minimum = min(f_value)

        self.print_algorithm_result(f_value, minimum, points)

    def find_minimum_value_n3(self):
        combinations = self.create_var_combinations(self.n)
        points = [(self.vars_dict[x], self.vars_dict[y], self.vars_dict[z]) for x, y, z in combinations]
        f_value = [self.example_function_n3(points[i]) for i in range(len(points))]
        minimum = min(f_value)

        while self.count_distance() > self.epsilon:
            self.iteration += 1
            self.calculate_a_b_value(f_value, minimum, combinations)
            self.calculate_x1_x2_value()

            points = [(self.vars_dict[x], self.vars_dict[y], self.vars_dict[z]) for x, y, z in combinations]
            f_value = [self.example_function_n3(points[i]) for i in range(len(points))]
            minimum = min(f_value)

        self.print_algorithm_result(f_value, minimum, points)

    def calculate_a_b_value(self, f_value, minimum, combinations):
        point = combinations[f_value.index(minimum)]
        change_dict = {
            'x1_': ['b_', 'x2_'],
            'x2_': ['a_', 'x1_']
        }

        for i in range(self.n):
            change_var = change_dict[point[i][:3]]
            self.vars_dict[change_var[0] + str(i)] = self.vars_dict[change_var[1] + str(i)]

    def print_algorithm_result(self, f_value, minimum, points):
        print(f'Minimum at the point: {points[f_value.index(minimum)]}')
        print(f'Minimum value: {minimum}')
        print(f'Number of iterations: {self.iteration}')

    def count_distance(self):
        distances = [pow(self.vars_dict[f'b_{i}'] - self.vars_dict[f'a_{i}'], 2) for i in range(self.n)]
        return sqrt(sum(distances))

    def calculate_x1_x2_value(self):
        for i in range(self.n):
            self.vars_dict[f'x1_{i}'] = self.vars_dict[f'a_{i}'] + (1 - self.k) * (
                    self.vars_dict[f'b_{i}'] - self.vars_dict[f'a_{i}'])
            self.vars_dict[f'x2_{i}'] = self.vars_dict[f'a_{i}'] + self.k * (
                    self.vars_dict[f'b_{i}'] - self.vars_dict[f'a_{i}'])

    @staticmethod
    def example_function_n1(variables):
        """Function has got minimum at x = 0.5."""
        return pow(variables - 0.5, 2) + 0.5

    @staticmethod
    def example_function_n2(variables):
        """Function has got minimum at x = 0.5 and y = 0.5."""
        return pow(variables[0] - 0.5, 4) + pow(variables[1] - 0.5, 4) + 2 * pow(variables[0] - 0.5, 2) + 2 * pow(
            variables[1] - 0.5, 2) + 4 * (variables[0] - 0.5) * (variables[1] - 0.5)

    @staticmethod
    def example_function_n3(variables):
        """Function has got minimum at (0, 0, 0)."""
        return pow(variables[0], 2) + pow(variables[1], 2) + pow(variables[2], 2)

    @staticmethod
    def create_var_combinations(n):
        var_list = [
            ['x1_0', 'x2_0'],
            ['x1_1', 'x2_1'],
            ['x1_2', 'x2_2'],
            ['x1_3', 'x2_3'],
            ['x1_4', 'x2_4']
        ]

        pools = [tuple(pool) for pool in var_list[:n]]
        result = [[]]
        for pool in pools:
            result = [x + [y] for x in result for y in pool]

        return result


if __name__ == '__main__':
    alg = Algorithm([0, 0, 0], [1, 1, 1], 2)
    # alg.find_minimum_value_n1()
    # alg.find_minimum_value_n2()
    alg.find_minimum_value_n3()
