import argparse

def main():
    # if there is an arg read from filename
    # else open interpreter
    parser = argparse.ArgumentParser(
                    prog='Lox',
                    description='Usage: jlox [script]',
                    )
    parser.add_argument('-f', '--filepath', required=False) 
    args = parser.parse_args()
    if args.filepath:
        runFile(args.filepath)
    else:
        runPrompt()

def runFile(filepath: str): 
    f = open(filepath)
    code = f.read()
    run(code)


def runPrompt():
    while True:
        print("> ")
        line = input()
        run(line)

def run(code:str):
    print(code)


if __name__ == "__main__":
    main()
