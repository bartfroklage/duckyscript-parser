from error import *

class Context:
    def __init__(self):
        self.variables = {}
    
    def set_variable(self, identifier: str, value: int):
        if identifier in self.variables:
            self.variables[identifier] = value
        else:
            raise RuntimeError(f'Variable {identifier} not initialized.')
    
    def init_variable(self, identifier: str, value: int):
        self.variables[identifier] = value
    
    def get_variable(self, identifier: str) -> int:
        if identifier in self.variables:
            return self.variables[identifier]
        else:
            raise RuntimeError(f'Variable {identifier} not initialized.')
    
