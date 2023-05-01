import re

class TokenInfo:
    def __init__(self, type_: str, pattern: str, skip: bool, has_value: bool, multi_line: bool):
        self.type = type_        
        self.pattern = re.compile(pattern, re.MULTILINE) if multi_line else re.compile(pattern)
        self.skip = skip
        self.has_value = has_value

TT_BOOLEAN      = 'BOOL'
TT_INT          = 'INT'
TT_STR          = 'STR'
TT_WHITESPACE   = 'WHITESPACE'
TT_VAR          = 'VAR'
TT_IDENTIFIER   = 'IDENTIFIER'
TT_EQUALS       = 'EQUALS'
TT_MIN          = 'MIN'
TT_PLUS         = 'PLUS'
TT_MULTIPLY     = 'MULTIPLY'
TT_DIVIDE       = 'DIVIDE'
TT_GREATER_THEN = '>'
TT_LESS_THEN    = '<'
TT_LPAREN       = 'LPAREN'
TT_RPAREN       = 'RPAREN'
TT_PRINT        = 'PRINT'
TT_REM          = 'REM'
TT_STRING       = 'STRING'
TT_STRINGLN     = 'STRINGLN'
TT_CURSORKEY    = 'CURSORKEY'
TT_SYSTEMKEY    = 'SYSTEMKEY'
TT_DELAY        = 'DELAY'
TT_IF           = 'IF'
TT_THEN         = 'THEN'
TT_ENDIF        = 'END_IF'
TT_ELSE         = 'ELSE'
TT_WHILE        = 'WHILE'
TT_ENDWHILE     = 'END_WHILE'


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
    TokenInfo(TT_PRINT, 'PRINT\s+', False, False, False),
    TokenInfo(TT_REM, 'REM (.*)', True, False, False),
    TokenInfo(TT_REM, 'REM_BLOCK ((.*\n*)*?)END_REM\s+', True, False, True),
    TokenInfo(TT_STRING, 'STRING (.*)', False, True, False), 
    TokenInfo(TT_STRING, 'STRING\n((.*\n*)*?)END_STRING\s+', False, True, True), 
    TokenInfo(TT_STRINGLN, 'STRINGLN (.*)', False, True, False), 
    TokenInfo(TT_STRINGLN, 'STRINGLN\n((.*\n*)*?)END_STRINGLN\s+', False, True, True),
    TokenInfo(TT_CURSORKEY, '(UP|DOWN|LEFT|RIGHT|UPARROW|DOWNARROW|LEFTARROW|RIGHTARROW|PAGEUP|PAGEDOWN|HOME|END|DEL|DELETE|BACKSPACE|TAB|SPACE)\s+', False, True, False),
    TokenInfo(TT_SYSTEMKEY, '(ENTER|ESCAPE|PAUSE|BREAK|PRINTSCREEN|MENU|APP|F1|F2|F3|F4|F5|F6|F7|F8|F9|F10|F11|F12)\s+', False, True, False),
    TokenInfo(TT_DELAY, 'DELAY', False, True, False),
    TokenInfo(TT_IF, 'IF', False, True, False),
    TokenInfo(TT_ENDIF, 'END_IF', False, False, False),
    TokenInfo(TT_THEN, 'THEN', False, False, False),
    TokenInfo(TT_ELSE, 'ELSE', False, False, False),
    TokenInfo(TT_WHILE, 'WHILE', False, False, False),
    TokenInfo(TT_ENDWHILE, 'END_WHILE', False, False, False)
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