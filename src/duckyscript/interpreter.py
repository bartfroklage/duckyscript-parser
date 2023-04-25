import sys
from tokenizer import *
from parser import *
from nodes import *
from error import *

class Interpreter:
    def __init__(self, script):
        self.script = script

    def run(self):
        return self.run_node(self.script)

    def run_node(self, node):
        if isinstance(node, BinOpNode): 
           return self.run_binop(node)
        elif isinstance(node, UnaryOpNode):
            return self.run_unaryop(node)
        elif isinstance(node, NumberNode):
            return int(node.value)

        return 1

    def run_binop(self, node: BinOpNode):
        operator = f'{node.operator}'
        left = self.run_node(node.left_node)
        right = self.run_node(node.right_node)

        if operator == TT_DIVIDE:
            return left / right
        elif operator == TT_MULTIPLY:
            return left * right
        elif operator == TT_MIN:
            return left - right
        elif operator == TT_PLUS:
            return left + right
       
    def run_unaryop(self, node: UnaryOpNode):
        operator = f'{node.operator}'
        right = self.run_node(node.right_node)

        if operator == TT_MIN:
            return -1 * right
        else:
            return right
        
if len(sys.argv) != 2:
    print('Please provide a filename.')
    exit(1)

script_file = open(sys.argv[1], 'r')
script = script_file.read()
script_file.close()

tokenizer = Tokenizer(script)
tokens = tokenizer.tokenize()

parser = Parser(tokens)
script = parser.parse()

interpreter = Interpreter(script)
print(interpreter.run())
