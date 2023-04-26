import re

class TokenInfo:
    def __init__(self, type_: str, pattern: str, skip: bool, has_value: bool, multi_line: bool):
        self.type = type_        
        self.pattern = re.compile(pattern, re.MULTILINE) if multi_line else re.compile(pattern)
        self.skip = skip
        self.has_value = has_value

TT_BOOLEAN      = 'BOOLEAN'
TT_INT          = 'INT'
TT_STRING       = 'STRING'
TT_WHITESPACE   = 'WHITESPACE'
TT_VAR          = 'VAR'
TT_IDENTIFIER   = 'IDENTIFIER'
TT_EQUALS       = 'EQUALS'
TT_MIN          = 'MIN'
TT_PLUS         = 'PLUS'
TT_MULTIPLY     = 'MULTIPLY'
TT_DIVIDE       = 'DIVIDE'
TT_LPAREN       = 'LPAREN'
TT_RPAREN       = 'RPAREN'
TT_PRINT        = 'PRINT'
TT_REM          = 'REM'

TOKENS_DATA = [
    TokenInfo(TT_BOOLEAN, 'TRUE|FALSE', False, True, False),
    TokenInfo(TT_INT, '\d+', False, True, False),
    TokenInfo(TT_STRING, '(\".*\")|(\'.*\')', False, True, False),
    TokenInfo(TT_WHITESPACE, '[\s]+', True, False, False),
    TokenInfo(TT_VAR, 'VAR', False, False, False),
    TokenInfo(TT_IDENTIFIER, '\$[A-Z]+', False, True, False),
    TokenInfo(TT_EQUALS, '=', False, False, False),
    TokenInfo(TT_MIN, '\-', False, False, False),
    TokenInfo(TT_PLUS, '\+', False, False, False),
    TokenInfo(TT_MULTIPLY, '\*', False, False, False),
    TokenInfo(TT_DIVIDE, '/', False, False, False),
    TokenInfo(TT_LPAREN, '\(', False, False, False),
    TokenInfo(TT_RPAREN, '\)', False, False, False),
    TokenInfo(TT_PRINT, 'PRINT', False, False, False),
    TokenInfo(TT_REM, 'REM (.*)', True, False, False),
    TokenInfo(TT_REM, 'REM_BLOCK ((.*\n*)*?)END_REM', True, False, True)
]

class PosInfo:
    def __init__(self, ln: int, col: int):
        self.ln = ln 
        self.col = col  
    def __repr__(self) -> str:
        return f'line: {self.ln}, column: {self.col}'

class Token:
    def __init__(self, type_: str, value: str, pos: PosInfo):
        self.type = type_
        self.value = value
        self.pos = pos

    def __repr__(self) -> str:
        if self.value:
            return f'{self.type}:{self.value}'
        else:
            return f'{self.type}'