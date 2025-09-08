from parser import Num, Var, BinOp, Assign

symbol_table = {}

def evaluate(node):
    if isinstance(node, Num):
        return node.value
    elif isinstance(node, Var):
        return symbol_table.get(node.name, 0)
    elif isinstance(node, BinOp):
        left_val = evaluate(node.left)
        right_val = evaluate(node.right)
        if node.op == 'PLUS':
            return left_val + right_val
        elif node.op == 'MINUS':
            return left_val - right_val
        elif node.op == 'MULT':
            return left_val * right_val
        elif node.op == 'DIV':
            return left_val / right_val
    elif isinstance(node, Assign):
        value = evaluate(node.expr)
        symbol_table[node.name] = value
        return value
