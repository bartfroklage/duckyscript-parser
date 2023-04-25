import ctypes

from tokens import *

class NumberNode:
    def __init__(self, value: int):
        self.value = value
        
    def __repr__(self):
        return f'{self.value}'


class BinOpNode:
    def __init__(self, left_node, operator: str, right_node):
        self.left_node = left_node
        self.operator = operator
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.operator}, {self.right_node})'
    
class UnaryOpNode:
    def __init__(self, operator, right_node):
        self.operator = operator
        self.right_node = right_node

    def __repr__(self):
        return f'({self.operator}, {self.right_node})'