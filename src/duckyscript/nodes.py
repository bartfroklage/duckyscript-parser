from tokens import *

class Node:
    def eval(self) -> int:
        pass

class NumberNode(Node):
    def __init__(self, value: int):
        super().__init__()
        self.value = value
        
    def __repr__(self):
        return f'{self.value}'
    
    def eval(self) -> int:
        return int(self.value)


class BinOpNode(Node):
    def __init__(self, left_node: Node, operator: str, right_node: Node):
        super().__init__()
        self.left_node = left_node
        self.operator = operator
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.operator}, {self.right_node})'
    
    def eval(self) -> int:
        super().__init__()
        operator = f'{self.operator}'
        if operator == TT_MIN:
            return self.left_node.eval() - self.right_node.eval()
        elif operator == TT_PLUS:
            return self.left_node.eval() + self.right_node.eval()
        elif operator == TT_MULTIPLY:
            return self.left_node.eval() * self.right_node.eval()
        elif operator == TT_DIVIDE:
            return self.left_node.eval() / self.right_node.eval()

class UnaryOpNode(Node):
    def __init__(self, operator, right_node: Node):
        super().__init__()
        self.operator = operator
        self.right_node = right_node

    def __repr__(self):
        return f'({self.operator}, {self.right_node})'

    def eval(self) -> int:
        operator = f'{self.operator}'
        if operator == TT_MIN:
            return -1 * self.right_node.eval()
        else:
            return self.right_node.eval()


class StatementNode:
    def __init__(self):
        pass

    def execute(self):
        pass


class AssignmentNode(StatementNode):
    def __init__(self, identifier: str, expr: Node, initialize: bool) -> None:
        super().__init__()
        self.identifier = identifier
        self.expr = expr
        self.initialize = initialize
    
    def execute(self):
        value = self.expr.eval()
        if 