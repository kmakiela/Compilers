#!/usr/bin/python


class Symbol(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Symbol: " + str(self.name)


class VariableSymbol(Symbol):

    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def __repr__(self):
        return "Variable Symbol: " + str(self.name) + ", type: " + str(self.type)


class FunctionSymbol(Symbol):
    def __init__(self, name, args):
        super().__init__(name)
        self.args = args


class ArraySymbol(VariableSymbol):
    def __init__(self, name, dimensions):
        super().__init__(name, 'matrix')
        self.dimensions = dimensions

    def __repr__(self):
        return "ArraySymbol: " + str(self.name) + ", dimensions: " + str(self.dimensions)


class SymbolTable(object):

    def __init__(self, parent, name):  # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.table = dict()
    #

    def put(self, name, symbol):  # put variable symbol or fundef under <name> entry
        self.table.update({name: symbol})
    #

    def get(self, name): # get variable symbol or fundef from <name> entry
        return self.table.get(name, None)
    #

    def getParentScope(self):
        return self.parent
    #

    def pushScope(self, name):
        pass
    #

    def popScope(self):
        pass
    #

    def display(self):
        print(self.table)


