import ctypes

from tokens import *

class IdentifierNode:
    def __init__(self):
        pass

class ExpressionNode:
    def __init__(self):
        pass


class ArithmeticExpressionNode(ExpressionNode):
    def __init___(self):
        super().__init__()
        pass

class StatementNode:
    def __init__(self):
        pass

class AssignmentNode(StatementNode):
    def __init__(self, identifier: IdentifierNode, expression: ExpressionNode, introduce: bool = False):
        super().__init__()
        self.identifier = identifier
        self.expression = expression
        self.introduce = introduce

class StatementsNode:
    def __init__(self, nodes: ctypes.Array = []):
        self.nodes = nodes
    
    def __repr__(self) -> str:
        result = ''
        for node in self.nodes:
            result = str(node) if (result == '') else result + '\n' + str(node)  
            
        return result

    def append(self, node: StatementNode):
        self.nodes.append(node)

        
    