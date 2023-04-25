import sys
from tokenizer import *
from parser import *
from nodes import *
from error import *

class Interpreter:
    def __init__(self, script):
        self.script = script

    def run(self):
        return self.script.eval()

   
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

print(script)
interpreter = Interpreter(script)
print(interpreter.run())
