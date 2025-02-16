from token import Token
class Scanner:
    def __init__(self, code) -> None:
        self.code = code
        self.tokens = []
        self.start = 0
        self.curr = 0
        self.line = 1

    def scanTokens(self) -> list[Token]:
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
        elif c == '!': self.addToken('BANG_EQUAL' if self.match('=') else 'BANG', c)
        elif c == '=': self.addToken('EQUAL_EQUAL' if self.match('=') else 'EQUAL', c)
        elif c == '<': self.addToken('LESS_EQUAL' if self.match('=') else 'LESS', c)
        elif c == '>': self.addToken('GREATER_EQUAL' if self.match('=') else 'GREATER', c)


        else: print(self.line, "Unexpected character.")
        
    def isAtEnd(self)->bool:
        return self.curr >= len(self.code)
    
    def advance(self)->str:
        c = self.code[self.curr]
        self.curr+=1
        return c

    def addToken(self,type:str,literal:str):
        text = self.code[self.start:self.curr]
        curr_token = Token(type,text,literal, self.line)
        self.tokens.append(curr_token)

    def match(self,expected:str)->bool:
        if self.isAtEnd() or self.code[self.curr] != expected:
            return False
        
        self.curr+=1
        return True
