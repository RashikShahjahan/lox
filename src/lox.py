class Lox():

    def __init__(self) -> None:
        pass

    def runFile(self,filepath: str): 
        f = open(filepath)
        code = f.read()
        self.run(code)


    def runPrompt(self):
        while True:
            print("> ")
            line = input()
            self.run(line)

    def run(self,code:str):
        print(code)


