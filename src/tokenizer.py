class Token:
    def __init__(self,type:str,lexeme:str, literal:str, line:int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __repr__(self) -> str:
        return f"{self.type} {self.lexeme} {self.literal}"