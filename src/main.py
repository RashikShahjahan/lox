import argparse
from lox import Lox

def main():

    parser = argparse.ArgumentParser(
                    prog='Lox',
                    description='Usage: jlox [script]',
                    )
    parser.add_argument('-f', '--filepath', required=False) 
    args = parser.parse_args()
    l = Lox()
    if args.filepath:
        l.runFile(args.filepath)
    else:
        l.runPrompt()

if __name__ == "__main__":
    main()
