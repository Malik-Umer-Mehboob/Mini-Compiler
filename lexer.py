import re

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.token_specification = [
            ('NUMBER', r'\d+'),
            ('ID', r'[a-zA-Z_]\w*'),
            ('ASSIGN', r'='),
            ('SEMICOLON', r';'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MULT', r'\*'),
            ('DIV', r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('SKIP', r'[ \t]+'),
            ('NEWLINE', r'\n'),
            ('MISMATCH', r'.')
        ]
        self.token_re = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specification))

    def tokenize(self):
        for mo in self.token_re.finditer(self.source_code):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                self.tokens.append(Token('NUMBER', int(value)))
            elif kind == 'ID':
                self.tokens.append(Token('ID', value))
            elif kind in ('ASSIGN', 'SEMICOLON', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPAREN'):
                self.tokens.append(Token(kind, value))
            elif kind in ('NEWLINE', 'SKIP'):
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Unexpected character: {value}')
        return self.tokens
