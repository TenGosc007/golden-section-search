from dataclasses import dataclass

"""Functions produces the value of a given type."""


@dataclass
class Number:
    value: float

    def __repr__(self):
        return f"{self.value}"


@dataclass
class Letter:
    value: str

    def __repr__(self):
        return f"{self.value}"
