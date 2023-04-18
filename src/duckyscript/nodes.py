import ctypes

from tokens import *

class IdentifierNode:
    def __init__(self):
        pass

class ArithmeticExpressionNode:
    def __init___(self):
        pass

class StatementNode:
    def __init__(self):
        pass

class NumberAssignmentNode(StatementNode):
    def __init__(self, identifier: IdentifierNode, expression: ArithmeticExpressionNode):
        super().__init__()
        self.identifier = identifier
        self.expression = expression

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

        
    