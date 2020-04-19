from src.nodes import *
from src.values import Number, Letter
from math import *

class Interpreter:
    def visit(self, node):
        """The function will process the tree and return a number / character"""
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_LetterNode(self, node):
        return Letter(node.value)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        if type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"{self.visit(node.node_a).value} + {self.visit(node.node_b).value}")
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        if type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"{self.visit(node.node_a).value} - {self.visit(node.node_b).value}")
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        if type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"{self.visit(node.node_a).value} * {self.visit(node.node_b).value}")
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_PowerNode(self, node):
        if type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"({self.visit(node.node_a).value}) ^ ({self.visit(node.node_b).value})")
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        if self.visit(node.node_b).value == 0.0:
            print(node)
        elif type(self.visit(node.node_a).value) == str or type(self.visit(node.node_b).value) == str:
            return Letter(f"{self.visit(node.node_a).value} / {self.visit(node.node_b).value}")
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def visit_PlusNode(self, node):
        if type(self.visit(node.node)) == str:
            return self.visit(node.node)
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"-{self.visit(node.node)}")
        return Number(-self.visit(node.node).value)

    def visit_SinusNode(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"sin({self.visit(node.node)})")
        return Number(sin(self.visit(node.node).value))

    def visit_CosinusNode(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"cos({self.visit(node.node)})")
        return Number(cos(self.visit(node.node).value))

    def visit_ExponentNode(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"exp({self.visit(node.node)})")
        return Number(exp(self.visit(node.node).value))

    def visit_SquareNode(self, node):
        if type(self.visit(node.node).value) == str:
            return Letter(f"sqrt({self.visit(node.node)})")
        return Number(sqrt(self.visit(node.node).value))