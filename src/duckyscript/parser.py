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
    
    def parse(self):
        return self.parse_script()

    def parse_script(self) -> ScriptNode:
        script = ScriptNode()
        while not self.eof():
            script.append_statement(self.parse_statement())
        return script

    def parse_statement(self):
        token = self.current_token()
        if token.type in (TT_VAR, TT_IDENTIFIER):
            return self.parse_assignment()
        elif token.type in (TT_PRINT):
            return self.parse_print()

        raise SyntaxError(f'Unexpected {token.type} at pos: {token.pos}.')
    
    def parse_assignment(self):
        token = self.current_token()
        initialize = False

        if token.type in (TT_VAR):
            initialize = True
            self.advance()
            token = self.current_token()
        
        if token.type not in (TT_IDENTIFIER):
            raise SyntaxError(f'Expected IDENTIFIER got {token.type} at pos {token.pos}.')
        
        identifier = token.value
        self.advance()

        token = self.current_token()
        if token.type not in (TT_EQUALS):
            raise SyntaxError(f'Expected EQUALS got {token.type} at pos {token.pos}.')

        self.advance()
        return AssignmentNode(identifier, self.parse_expr(), initialize)
        
    def parse_print(self):
        token = self.current_token()

        if token.type not in (TT_PRINT):
            raise SyntaxError(f'Expected PRINT got {token.type} at pos {token.pos}.')
        self.advance()
        return PrintNode(self.parse_expr())
        
    def parse_factor(self):
        token = self.current_token()

        if token.type in (TT_PLUS, TT_MIN):
            operator = token.type
            self.advance()
            return UnaryOpNode(operator, self.parse_factor())

        elif token.type in (TT_INT):
            self.advance()
            return NumberNode(token.value)

        elif token.type in (TT_IDENTIFIER):
            self.advance()
            return IdentifierNode(token.value)
        
        elif token.type in (TT_LPAREN):
            self.advance()
            expr = self.parse_expr()
            token = self.current_token()
            if token.type not in(TT_RPAREN):
                raise SyntaxError('Expected ) got {} at pos {}.'.format(token.type, token.pos))
            self.advance()
            return expr
            
        raise SyntaxError('Expected INT got {} at pos {}.'.format(token.type, token.pos))
    
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