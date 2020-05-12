from math import sqrt

import numpy as np


class Algorithm:
    def __init__(self, x0, d, n, epsilon, stop, stop_iteration, function, logger):
        self.logger = logger
        self.epsilon = epsilon
        self.k = (sqrt(5) - 1) / 2
        self.n = n
        self.stop = stop
        self.stop_iteration = stop_iteration
        self.function = function
        self.a, self.b = self.get_range(x0, d)
        self.vars_dict = self.get_vars_dict(self.n)
        self.iteration = 0
        self.min_value = None

    def get_range(self, x0, d):
        """Function returns a and b."""
        x0 = np.array(x0)
        d = np.array(d)
        f = self.function

        step = 0.01 * np.sqrt(d * d.transpose())
        i = 0
        y0 = f(x0)
        while i < 2:
            x = x0 + step * d
            y = f(x)
            if y0 <= y:
                step = -step
                i += 1
            else:
                while y0 > y:
                    step = 2 * step
                    y0 = y
                    x = x + step * d
                    y = f(x)
                i = 1
                break
        x2 = x
        x1 = x0 + step * (i - 1) * d
        a = d * (x1 - x0) / (d * d.transpose())
        b = d * (x2 - x0) / (d * d.transpose())
        self.logger.append(f'\nDługość przedziału: a = {a}, b = {b}\n\n')
        return a, b

    def get_vars_dict(self, n):
        """Function initialises vars for algorithm."""
        vars_dict = {}
        for i in range(n):
            vars_dict[f'a_{i}'] = self.a[i]
            vars_dict[f'b_{i}'] = self.b[i]
            vars_dict[f'x1_{i}'] = self.a[i] + (1 - self.k) * (self.b[i] - self.a[i])
            vars_dict[f'x2_{i}'] = self.a[i] + self.k * (self.b[i] - self.a[i])

        return vars_dict

    def stop_condition(self, previous_min, current_min, prev_fmin, curr_fmin):
        """Function performing the stop criterion"""
        if previous_min != current_min:
            if self.stop == 0:
                stop = abs(abs(current_min - previous_min))
                return stop
            elif self.stop == 1:
                stop = abs(curr_fmin - prev_fmin)
                return stop
            elif self.stop == 2:
                if self.iteration == self.stop_iteration:
                    return 0
                elif self.stop_iteration == 0:
                    return 0
                else:
                    return None
        return None

    def find_minimum_value(self):
        """Function prints minimum value for math function."""
        self.logger.append('------------------------ Działanie algorytmu ------------------------')
        combinations = self.create_var_combinations()
        points = [self.get_points(var_list) for var_list in combinations]
        f_value = [self.function(points[i]) if self.n > 1 else self.function(points[i][0]) for i in
                   range(len(points))]
        minimum = min(f_value)

        current_min = points[f_value.index(minimum)][0]

        while True:
            previous_min = current_min
            prev_fmin = minimum
            self.iteration += 1
            self.calculate_a_b_value(f_value, minimum, combinations)
            self.calculate_x1_x2_value()

            points = [self.get_points(var_list) for var_list in combinations]
            f_value = [self.function(points[i]) if self.n > 1 else self.function(points[i][0]) for i in
                       range(len(points))]
            minimum = min(f_value)
            self.print_algorithm_result(f_value, minimum, points)

            current_min = points[f_value.index(minimum)][0]
            stop = self.stop_condition(previous_min, current_min, prev_fmin, minimum)
            if stop is not None and stop <= self.epsilon:
                break

        self.logger.append('\n------------------------ Wyniki ------------------------')
        self.print_algorithm_result(f_value, minimum, points)
        self.min_value = points[f_value.index(minimum)]

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
        self.logger.append(f'\nNumer iteracji: {self.iteration}\n\n'
                           f'Minimum znajduje się w punktcie:\n{points[f_value.index(minimum)]}\n\n'
                           f'Minimalna wartość: {minimum}\n\n'
                           f'------------------------------------------------------------')
