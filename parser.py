class ASTNode:
    pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class Var(ASTNode):
    def __init__(self, name):
        self.name = name

class Assign(ASTNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self, expected_type=None):
        token = self.tokens[self.pos]
        if expected_type and token.type != expected_type:
            raise RuntimeError(f'Expected {expected_type}, got {token.type}')
        self.pos += 1
        return token

    def parse(self):
        nodes = []
        while self.pos < len(self.tokens):
            nodes.append(self.assignment())
        return nodes

    def assignment(self):
        var_name = self.consume('ID').value
        self.consume('ASSIGN')
        expr = self.expr()
        self.consume('SEMICOLON')
        return Assign(var_name, expr)

    def expr(self):
        node = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in ('PLUS', 'MINUS'):
            op = self.consume().type
            node = BinOp(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in ('MULT', 'DIV'):
            op = self.consume().type
            node = BinOp(node, op, self.factor())
        return node

    def factor(self):
        token = self.consume()
        if token.type == 'NUMBER':
            return Num(token.value)
        elif token.type == 'ID':
            return Var(token.value)
        elif token.type == 'LPAREN':
            node = self.expr()
            self.consume('RPAREN')
            return node
        else:
            raise RuntimeError(f'Unexpected token: {token.type}')
