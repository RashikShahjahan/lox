from tokenizer import Token
class Scanner:
    def __init__(self, code) -> None:
        self.code = code
        self.tokens = []
        self.start = 0
        self.curr = 0
        self.line = 1
        self.keywords = {
            "and": 'AND',
            "class": 'CLASS',
            "else": 'ELSE',
            "false": 'FALSE',
            "for": 'FOR',
            "fun": 'FUN',
            "if": 'IF',
            "nil": 'NIL',
            "or": 'OR',
            "print": 'PRINT',
            "return": 'RETURN',
            "super": 'SUPER',
            "this": 'THIS',
            "true": 'TRUE',
            "var": 'VAR',
            "while": 'WHILE',
        }

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
        elif c == ' ' or c == '\t' or c== '\r':
            pass
        elif c == '\n':
            self.line+=1
        elif c == '"':
            self.string()
        elif c.isdigit():
            self.number()
        elif c.isalpha():
            self.identifier()
        else: print(self.line, "Unexpected character.")

    def string(self):
        while self.peek() != '"' and not self.isAtEnd():
            if self.peek() == '\n':
                self.line+=1
            self.advance()

        if self.isAtEnd():
            print(self.line, "Unterminated string.")
            return

        self.advance()

        value = self.code[self.start+1:self.curr-1]
        self.addToken('STRING', value)

    def number(self):
        while self.peek().isdigit():self.advance()

        if self.peek() == '.' and self.peekNext().isdigit():
            self.advance()
            while self.peek().isdigit():self.advance()

        self.addToken('NUMBER',float(self.code[self.start:self.curr]))

    def identifier(self):
        while self.peek().isalnum():self.advance()
        text = self.code[self.start:self.curr]
        type = self.keywords.get(text,'IDENTIFIER')
        self.addToken(type)


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

    def peek(self)->str:
        if (self.isAtEnd()): return '\0'
        return self.code[self.curr]
    
    def peekNext(self)->str:
        if self.curr+1 >= len(self.code):
            return '\0'
        return self.code[self.curr+1]
       