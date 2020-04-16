from dataclasses import dataclass

@dataclass
class NumberNode:
    value: float
    def __repr__(self):
        return f"{self.value}"

@dataclass
class LetterNode:
    value: str
    def __repr__(self):
        return f"{self.value}"

@dataclass
class IndexNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}{self.node_b})"

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"

@dataclass
class PowerNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}^{self.node_b})"

@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"

@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"

@dataclass
class SinusNode:
    node: any

    def __repr__(self):
        return f"sin({self.node})"

@dataclass
class CosinusNode:
    node: any

    def __repr__(self):
        return f"cos({self.node})"

@dataclass
class ExponentNode:
    node: any

    def __repr__(self):
        return f"exp({self.node})"

@dataclass
class SquareNode:
    node: any

    def __repr__(self):
        return f"sqrt({self.node})"
        
