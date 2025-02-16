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
        if c == '(': self.addToken('LEFT_PAREN')
        elif c == ')': self.addToken('RIGHT_PAREN')
        elif c == '{': self.addToken('LEFT_BRACE')
        elif c == '}': self.addToken('RIGHT_BRACE')
        elif c == ',': self.addToken('COMMA')
        elif c == '.': self.addToken('DOT')
        elif c == '-': self.addToken('MINUS')
        elif c == '+': self.addToken('PLUS')
        elif c == ';': self.addToken('SEMICOLON')
        elif c == '*': self.addToken('STAR')
        elif c == '!': self.addToken('BANG_EQUAL' if self.match('=') else 'BANG')
        elif c == '=': self.addToken('EQUAL_EQUAL' if self.match('=') else 'EQUAL')
        elif c == '<': self.addToken('LESS_EQUAL' if self.match('=') else 'LESS')
        elif c == '>': self.addToken('GREATER_EQUAL' if self.match('=') else 'GREATER')
        elif c == '/':
            if self.match('/'):
                while self.peek() != '\n' and not self.isAtEnd():
                    self.advance()
            else:
                self.addToken('SLASH')


        else: print(self.line, "Unexpected character.")
        
    def isAtEnd(self)->bool:
        return self.curr >= len(self.code)
    
    def advance(self)->str:
        c = self.code[self.curr]
        self.curr+=1
        return c

    def addToken(self,type:str,literal:str=None):
        text = self.code[self.start:self.curr]
        curr_token = Token(type,text,literal, self.line)
        self.tokens.append(curr_token)

    def match(self,expected:str)->bool:
        if self.isAtEnd() or self.peek() != expected:
            return False
        
        self.curr+=1
        return True

    def peek(self):
        if (self.isAtEnd()): return '\0'
        return self.code[self.curr]