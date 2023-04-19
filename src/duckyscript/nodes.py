import ctypes

from tokens import *

class IdentifierNode:
    def __init__(self, id: str):
        self.id = id
    
    def __repr__(self) -> str:
        return f'{self.id}'

class ExpressionNode:
    def __init__(self):
        pass

class ArithmeticExpressionNode(ExpressionNode):
    def __init___(self):
        super().__init__()
        pass

class ArchimeticFactorNode:
    def __init___(self, minus: bool, identifier: IdentifierNode, number: int, expression: ArithmeticExpressionNode):
        self.identifier = identifier
        self.expression = expression
        self.number = number
        self.minus = minus

    def __repr__(self) -> str:
        sign = '-' if self.minus else ''
        
        if self.identifier is not None:
            return f'{sign}{self.identifier}'
        
        if self.expression is not None:
            return f'{sign}{self.expression}'

        return f'{sign}{self.number}'




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

        
    