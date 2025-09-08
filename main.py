from tabulate import tabulate
from lexer import Lexer
from parser import Parser
from evaluator import evaluate, symbol_table

if __name__ == '__main__':
    print("Enter your code (end with an empty line):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    source = '\n'.join(lines)

    # Step 1: Lexer
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    token_rows = [[token.type, token.value] for token in tokens]
    print("\nTokens (Lexical Analysis):")
    print(tabulate(token_rows, headers=["Token Type", "Token Value"], tablefmt="grid"))

    # Step 2: Parser
    parser = Parser(tokens)
    ast = parser.parse()

    # Step 3: Evaluation
    print("\nEvaluation Results:")
    for node in ast:
        result = evaluate(node)
        print(f"{node.name} = {result}")

    print("\nSymbol Table:", symbol_table)
