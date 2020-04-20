from math import *

from src.values import Number, Letter


class Interpreter:
    def visit(self, node):
        """The function will process the tree and return a number / character"""
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    @staticmethod
    def visit_letter_node(node):
        return Letter(node.value)

    @staticmethod
    def visit_number_node(node):
        return Number(node.value)

    def visit_add_node(self, node):
        if type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"{self.visit(node.node_a).value} + {self.visit(node.node_b).value}")
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_subtract_node(self, node):
        if type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"{self.visit(node.node_a).value} - {self.visit(node.node_b).value}")
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_multiply_node(self, node):
        if type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"{self.visit(node.node_a).value} * {self.visit(node.node_b).value}")
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_power_node(self, node):
        if type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"({self.visit(node.node_a).value}) ^ ({self.visit(node.node_b).value})")
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

    def visit_divide_node(self, node):
        if self.visit(node.node_b).value == 0.0:
            print(node)
        elif type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"{self.visit(node.node_a).value} / {self.visit(node.node_b).value}")
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except Exception:
            raise Exception("Runtime math error")

    def visit_plus_node(self, node):
        if type(self.visit(node.node)) == str:
            return self.visit(node.node)
        return self.visit(node.node)

    def visit_minus_node(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"-{self.visit(node.node)}")
        return Number(-self.visit(node.node).value)

    def visit_sinus_node(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"sin({self.visit(node.node)})")
        return Number(sin(self.visit(node.node).value))

    def visit_cosinus_node(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"cos({self.visit(node.node)})")
        return Number(cos(self.visit(node.node).value))

    def visit_exponent_node(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"exp({self.visit(node.node)})")
        return Number(exp(self.visit(node.node).value))

    def visit_square_node(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"sqrt({self.visit(node.node)})")
        return Number(sqrt(self.visit(node.node).value))
