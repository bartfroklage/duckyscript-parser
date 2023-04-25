import ctypes
from nodes import *
from error import *
from tokens import *

class Parser:
    def __init__(self, tokens: ctypes.Array):
        self.tokens = tokens
        self.token_idx = 0
    
    def current_token(self) -> Token:
        if len(self.tokens) > self.token_idx:
            return self.tokens[self.token_idx]
        else:
            return None
    
    def advance(self):
        self.token_idx += 1

    def eof(self) -> bool:
        return len(self.tokens) <= self.token_idx
    
    def parse_factor(self):
        token = self.current_token()

        if token.type in (TT_PLUS, TT_MIN):
            operator = token.type
            self.advance()
            if self.eof():
                raise SyntaxError('Expected INT got EOF at pos {}.'.format(token.pos))
            token = self.current_token()
            if token.type not in(TT_INT):
                raise SyntaxError('Expected INT got {} at pos {}.'.format(token.type, token.pos))
            
            return UnaryOpNode(operator, token.value)

        elif token.type in (TT_INT):
            self.advance()
            return NumberNode(token.value)
        
        elif token.type in (TT_LPAREN):
            self.advance()
            expr = self.parse_expr()
            token = self.current_token()
            if token.type not in(TT_RPAREN):
                raise SyntaxError('Expected ) got {} at pos {}.'.format(token.type, token.pos))
            self.advance()
            return expr
            
        raise SyntaxError('Expected INT got {} at pos {}.'.format(token.type, token.pos))
    
    def parse(self):
        return self.parse_expr()

    def parse_term(self):
        return self.parse_binop(self.parse_factor, (TT_MULTIPLY, TT_DIVIDE))
    
    def parse_expr(self):
        return self.parse_binop(self.parse_term, (TT_MIN, TT_PLUS))
    

    def parse_binop(self, func, ops):
        left = func()
        while not self.eof() and self.current_token().type in ops:
            operator_token = self.current_token()
            self.advance()

            right = func()
            left = BinOpNode(left, operator_token, right)
        
        return left