import sys
from scanner import Scanner

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

        for token in tokens:
            print(token)
        

    def reportError(self,line:int, message:str):
        print(f"[line {line}] Error: {message}")
        self.hadError = True





