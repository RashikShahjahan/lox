import argparse

def main():
    # if there is an arg read from filename
    # else open interpreter
    parser = argparse.ArgumentParser(
                    prog='Lox',
                    description='Usage: jlox [script]',
                    )
    parser.add_argument('-f', '--filename', required=False) 
    args = parser.parse_args()
    if args.filename:
        print(args.filename)
        runFile()
    else:
        runPrompt()

def runFile():
    pass


def runPrompt():
    pass


if __name__ == "__main__":
    main()
