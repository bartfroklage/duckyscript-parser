import ctypes

from error import *
from tokens import *

class Tokenizer:
    def __init__(self, text: str):
        self.text = text
    
    def pos_info(self, pos: int) -> PosInfo:
        col = 0
        ln = 0
       
        for ix in range(pos):                           
            if self.text[ix] == '\n':
                ln += 1
                col = 1
            else:
                col += 1
        return PosInfo(ln, col)
   
    def tokenize(self) -> ctypes.Array:
        tokens = []

        pos = 0
        while pos < len(self.text):
            
            invalid_char = True
            for tokenData in TOKENS_DATA:
                
                if match := tokenData.pattern.match(self.text, pos):
                    invalid_char = False

                    if tokenData.skip:
                        pos = match.end()
                        break
                    
                    token = Token(tokenData.type, match.group(0) if tokenData.has_value else '',  self.pos_info(pos))
                    tokens.append(token)
                    pos = match.end()
                    break

            if invalid_char:
                posInfo = self.pos_info(pos)
                chr = self.text[pos]
                raise IllegalCharError('Unexpected \'{}\' at {}.'.format(chr, posInfo))
        
        return tokens
