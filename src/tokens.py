from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    LETTER = 7
    POWER = 8
    SIN = 9
    COS = 10
    EXP = 11
    SQRT = 12
    LBRACKET = 13
    RBRACKET = 14


@dataclass
class Token:
    """Class returns tokens."""
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
