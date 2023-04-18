import ctypes
from nodes import *
from error import *
from tokens import *

class Parser:
    def __init__(self, tokens: ctypes.Array):
        self.tokens = tokens
        self.idx = 0
    
    def peek_token(self) -> Token:
        if self.eof(): return None
        return self.tokens[self.idx]
    
    def pop_token(self) -> Token:
        if self.eof(): return None
        token = self.tokens[self.idx]
        self.idx += 1
        return token
    
    def eof(self) -> bool:
        return len(self.tokens) <= self.idx 

    def parse(self) -> StatementsNode:
        script = StatementsNode()
        while not(self.eof()):
            script.append(self.parse_statement())
        return script
    
    def parse_statement(self) -> StatementNode:
        token = self.peek_token()
        if token.type in (TT_IDENTIFIER, TT_VAR):
            return self.parse_assignment()
        raise InvalidSyntaxError('Unexpected token at {}.'.format(token.pos))
    
    def parse_assignment(self) -> AssignmentNode:
        token = self.peek_token()

        introduce = (token.type == TT_VAR)
        if introduce: self.pop_token()

        identifier_token = self.pop_token()
        if identifier_token.type != TT_IDENTIFIER:
            raise InvalidSyntaxError('Unexpected token at {}, expected IDENTIFIER got {}.'.format(token.pos, identifier_token.type))

        expression = self.parse_expression()
        return AssignmentNode()
    
    def parse_expression(self) -> ExpressionNode:
        pass

            