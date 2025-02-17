from abc import ABC
from tokenizer import Token

class Expr(ABC):
    pass

class Binary(Expr):
    def __init__(self,left:Expr,operator:Token,right:Expr) -> None:
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self) -> str:
        return f"({self.operator.lexeme} {self.left} {self.right})"

class Grouping(Expr):
    def __init__(self,expression:Expr) -> None:
        self.expression = expression

    def __repr__(self) -> str:
        return f"(group {self.expression})"

class Literal(Expr):
    def __init__(self,value:object) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value}"

class Unary(Expr):
    def __init__(self,operator:Token,right:Expr) -> None:
        self.operator = operator
        self.right = right

    def __repr__(self) -> str:
        return f"({self.operator.lexeme} {self.right})"


