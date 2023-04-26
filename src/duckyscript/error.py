class Error(Exception):
    def __init__(self, error_name: str, details: str): 
        self.error_name = error_name
        self.details = details

    def __repr__(self) -> str:
        return f'{self.error_name}: {self.details}'
    
class IllegalCharError(Error):
    def __init__(self, details: str):
        super().__init__('Illegal Character', details)

class SyntaxError(Error):
    def __init__(self, details: str):
        super().__init__('Syntax Error', details)

class RuntimeError(Error):
    def __init__(self, details: str):
        super().__init__('Runtime exception', details)