class CodeBase:
    def __init__(self):
        self.code_modules = []

    def add_code_module(self, code_module):
        self.code_modules.append(code_module)

    def remove_code_module(self, code_module):
        self.code_modules.remove(code_module)
