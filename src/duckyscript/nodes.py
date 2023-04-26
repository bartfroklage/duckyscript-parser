from tokens import *
from context import *

class Node:
    def eval(self, context: Context) -> int:
        pass

class NumberNode(Node):
    def __init__(self, value: int):
        super().__init__()
        self.value = value
        
    def __repr__(self):
        return f'{self.value}'
    
    def eval(self, context: Context) -> int:
        return int(self.value)

class IdentifierNode(Node):
    def __init__(self, identifier: str):
        super().__init__()
        self.identifier = identifier
        
    def __repr__(self):
        return f'{self.identifier}'
    
    def eval(self, context: Context) -> int:
        return int(context.get_variable(self.identifier))

class BinOpNode(Node):
    def __init__(self, left_node: Node, operator: str, right_node: Node):
        super().__init__()
        self.left_node = left_node
        self.operator = operator
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.operator}, {self.right_node})'
    
    def eval(self, context: Context) -> int:
        super().__init__()
        operator = f'{self.operator}'
        if operator == TT_MIN:
            return self.left_node.eval(context) - self.right_node.eval(context)
        elif operator == TT_PLUS:
            return self.left_node.eval(context) + self.right_node.eval(context)
        elif operator == TT_MULTIPLY:
            return self.left_node.eval(context) * self.right_node.eval(context)
        elif operator == TT_DIVIDE:
            return self.left_node.eval(context) / self.right_node.eval(context)

class UnaryOpNode(Node):
    def __init__(self, operator, right_node: Node):
        super().__init__()
        self.operator = operator
        self.right_node = right_node

    def __repr__(self):
        return f'({self.operator}, {self.right_node})'

    def eval(self, context: Context) -> int:
        operator = f'{self.operator}'
        if operator == TT_MIN:
            return -1 * self.right_node.eval(context)
        else:
            return self.right_node.eval(context)

class StatementNode:
    def __init__(self):
        pass

    def execute(self, context: Context):
        pass

class ScriptNode:
    def __init__(self):
        self.statements = []

    def execute(self, context: Context):
        for statement in self.statements:
            statement.execute(context)
    
    def append_statement(self, statement: StatementNode):
        self.statements.append(statement)

class AssignmentNode(StatementNode):
    def __init__(self, identifier: str, expr: Node, initialize: bool) -> None:
        super().__init__()
        self.identifier = identifier
        self.expr = expr
        self.initialize = initialize
    
    def execute(self, context: Context):
        value = self.expr.eval(context)
        
        if self.initialize:
            context.init_variable(self.identifier, value)
        else:
            context.set_variable(self.identifier, value)

class PrintNode(StatementNode):
    def __init__(self, expr: Node):
        super().__init__()
        self.expr = expr
    
    def execute(self, context: Context):
        print(self.expr.eval(context))

