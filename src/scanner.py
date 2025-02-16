from token import Token
class Scanner:
    def __init__(self, code) -> None:
        self.code = code
        self.tokens = []
        self.start = 0
        self.curr = 0
        self.line = 1

    def scanTokens(self) -> None:
        while not self.isAtEnd():
            self.start = self.curr
            self.scanToken()
        eof_token = Token('EOF', "", None, self.line)
        self.tokens.append(eof_token);
        return self.tokens
    
    def scanToken(self) -> None:
        c = self.advance()
        if c == '(': self.addToken('LEFT_PAREN', c)
        elif c == ')': self.addToken('RIGHT_PAREN', c)
        elif c == '{': self.addToken('LEFT_BRACE', c)
        elif c == '}': self.addToken('RIGHT_BRACE', c)
        elif c == ',': self.addToken('COMMA', c)
        elif c == '.': self.addToken('DOT', c)
        elif c == '-': self.addToken('MINUS', c)
        elif c == '+': self.addToken('PLUS', c)
        elif c == ';': self.addToken('SEMICOLON', c)
        elif c == '*': self.addToken('STAR', c)
        else: print(self.line, "Unexpected character.")
        
    def isAtEnd(self)->bool:
        return self.curr >= len(self.code)
    
    def advance(self)->str:
        c = self.code[self.curr]
        self.curr+=1
        return c

    def addToken(self,type:str,literal:str):
        text = self.code[self.start:self.curr+1]
        curr_token = Token(type,text,literal, self.line)
        self.tokens.append(curr_token)