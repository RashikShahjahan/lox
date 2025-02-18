import sys
from scanner import Scanner
from parser import Parser

class Lox:

    def __init__(self) -> None:
        self.hadError = False

    def runFile(self,filepath: str): 
        f = open(filepath)
        code = f.read()
        self.run(code)
        if self.hadError:
            sys.exit(65)


    def runPrompt(self):
        while True:
            print("> ")
            line = input()
            self.run(line)
            self.hadError = False

    def run(self,code:str):
        scanner = Scanner(code)
        tokens = scanner.scanTokens()
        print(tokens)
        p = Parser(tokens)

        expression = p.parse()
        print(expression)


        

    def reportError(self,line:int, message:str):
        print(f"[line {line}] Error: {message}")
        self.hadError = True





