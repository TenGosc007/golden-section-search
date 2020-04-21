from math import sqrt

from src.utils import example_function_n5


class Algorithm:
    def __init__(self, a, b, n, function):
        self.epsilon = 0.001
        self.k = (sqrt(5) - 1) / 2
        self.n = n
        self.vars_dict = self.get_vars_dict(a, b, self.n)
        self.function = function
        self.iteration = 0

    def get_vars_dict(self, a, b, n):
        """Function initialises vars for algorithm."""
        vars_dict = {}
        for i in range(n):
            vars_dict[f'a_{i}'] = a[i]
            vars_dict[f'b_{i}'] = b[i]
            vars_dict[f'x1_{i}'] = a[i] + (1 - self.k) * (b[i] - a[i])
            vars_dict[f'x2_{i}'] = a[i] + self.k * (b[i] - a[i])

        return vars_dict

    def find_minimum_value(self):
        """Function prints minimum value for math function."""
        combinations = self.create_var_combinations()
        points = [self.get_points(var_list) for var_list in combinations]
        f_value = [self.function(points[i]) if self.n > 1 else self.function(points[i][0]) for i in
                   range(len(points))]
        minimum = min(f_value)

        while self.count_distance() > self.epsilon:
            self.iteration += 1
            self.calculate_a_b_value(f_value, minimum, combinations)
            self.calculate_x1_x2_value()

            points = [self.get_points(var_list) for var_list in combinations]
            f_value = [self.function(points[i]) if self.n > 1 else self.function(points[i][0]) for i in
                       range(len(points))]
            minimum = min(f_value)

        self.print_algorithm_result(f_value, minimum, points)

    def create_var_combinations(self):
        """Function creates 2^n combinations of available variables."""
        vars_list = [[f'x1_{i}', f'x2_{i}'] for i in range(self.n)]
        pools = [tuple(pool) for pool in vars_list]
        result = [[]]
        for pool in pools:
            result = [x + [y] for x in result for y in pool]
        return result

    def get_points(self, var_list):
        """Function gets points for list of variables."""
        return [self.vars_dict[i] for i in var_list]

    def count_distance(self):
        """Function returns value of Euclidean metric for algorithm points."""
        distances = [pow(self.vars_dict[f'b_{i}'] - self.vars_dict[f'a_{i}'], 2) for i in range(self.n)]
        return sqrt(sum(distances))

    def calculate_a_b_value(self, f_value, minimum, combinations):
        """Function calculates a and b value based on points x1 and x2."""
        point = combinations[f_value.index(minimum)]
        change_dict = {
            'x1_': ['b_', 'x2_'],
            'x2_': ['a_', 'x1_']
        }
        for i in range(self.n):
            change_var = change_dict[point[i][:3]]
            self.vars_dict[change_var[0] + str(i)] = self.vars_dict[change_var[1] + str(i)]

    def calculate_x1_x2_value(self):
        """Function calculates x1 and x2 value for algorithm."""
        for i in range(self.n):
            self.vars_dict[f'x1_{i}'] = self.vars_dict[f'a_{i}'] + (1 - self.k) * (
                    self.vars_dict[f'b_{i}'] - self.vars_dict[f'a_{i}'])
            self.vars_dict[f'x2_{i}'] = self.vars_dict[f'a_{i}'] + self.k * (
                    self.vars_dict[f'b_{i}'] - self.vars_dict[f'a_{i}'])

    def print_algorithm_result(self, f_value, minimum, points):
        """Function prints algorithm results."""
        print(f'Minimum at the point: {points[f_value.index(minimum)]}')
        print(f'Minimum value: {minimum}')
        print(f'Number of iterations: {self.iteration}')


if __name__ == '__main__':
    alg = Algorithm([0, 0, 0, 0, 0], [1, 1, 1, 1, 1], 5, example_function_n5)
    alg.find_minimum_value()
