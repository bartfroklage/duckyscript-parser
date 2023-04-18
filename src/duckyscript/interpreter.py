import sys
from tokenizer import *
from parser import *

if len(sys.argv) != 2:
    print('Please provide a filename.')
    exit(1)

script_file = open(sys.argv[1], 'r')
script = script_file.read()
script_file.close()

tokenizer = Tokenizer(script)
tokens =  tokenizer.tokenize()

parser = Parser(tokens)
script = parser.parse_script()
print(script)