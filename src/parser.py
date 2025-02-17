from typing import List
from tokenizer import Token
from expr import Expr, Binary, Unary, Literal, Grouping

class Parser:
    def __init__(self, tokens:List[Token]) -> None:
        self.tokens = tokens
        self.curr = 0

    
    def parse(self)->Expr:
        expr = self.expression()
        return expr

    def expression(self)->Expr:
        expr = self.equality()
        return expr
        
    def equality(self)->Expr:
        expr = self.comparison()
        while (self.match(['BANG_EQUAL', 'EQUAL_EQUAL'])):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr
    
    def comparison(self)->Expr:
        expr = self.term()
        while (self.match(['GREATER', 'GREATER_EQUAL', 'LESS', 'LESS_EQUAL'])):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)

        return expr
    
    def term(self)->Expr:
        expr = self.factor()
        while (self.match(['MINUS', 'PLUS'])):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr
    
    def factor(self)->Expr:
        expr = self.unary()

        while (self.match(['SLASH', 'STAR'])):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr
    
        
    def unary(self)->Expr:
        if (self.match(['BANG', 'MINUS'])):
            operator = self.previous()
            right = self.unary()
            expr = Unary(operator, right)

            return expr

        return self.primary();


    def primary(self)->Expr:
        if self.match(['FALSE']): return Literal(False)
        if self.match(['TRUE']): return Literal(True)
        if self.match(['NIL']): return Literal(None)
        if self.match(['NUMBER','STRING']): return Literal(self.previous().literal)


        if self.match(['LEFT_PAREN']):
            expr = self.expression();
            self.consume('RIGHT_PAREN', "Expect ')' after expression.");

            return Grouping(expr)
        



    
    def match(self, types:List[str])->bool:
        for type in types:
            if (self.check(type)):
                self.advance()
                return True
        return False
    
    def advance(self)->Token:
        if not self.isAtEnd():
            self.curr+=1
        return self.previous()
    
    def check(self,type:str)->bool:
        if self.isAtEnd():
            return False
        
        return self.peek().type == type

    def isAtEnd(self)->bool:
        return self.peek().type == 'EOF'
    
    def peek(self)->Token:
        return self.tokens[self.curr]
    
    def previous(self)->Token:
        return self.tokens[self.curr-1]
    
    def consume(self, type:str, message:str)->Token:
        if self.check(type):
            return self.advance()
        
        raise self.error(self.peek(), message)

    def error(self,token:Token, message:str):
        return ParseError()
    
    def synchronize(self):
        self.advance()

        while (not self.isAtEnd()):
            if (self.previous().type == 'SEMICOLON'): 
                return

            if (self.peek().type in ['CLASS', 'FUN', 'VAR', 'FOR', 'IF', 'WHILE', 'PRINT', 'RETURN']):
                return

            self.advance()



class ParseError(Exception):
    pass