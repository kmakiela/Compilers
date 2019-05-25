#!/usr/bin/python
import SyntaxTree.AST as AST
from SemanticsCheck.SymbolTable import *
from collections import defaultdict


INT = 'int'
FLOAT = 'float'
MATRIX = 'matrix'
VECTOR = 'vector'
STRING = 'string'
BOOL = 'bool'
arithmetic_operators = ['+', '-', '*', '/']
dot_operators = ['.+', '.-', '.*', './']
comparison_operators = ['<', '>', '<=', '>=', '!=', '==']
assign_operators = ['+=', '-=', '*=', '/=']


class Operations(object):
    def __init__(self):
        self.possible_types = defaultdict(lambda: defaultdict(dict))

        for op in arithmetic_operators + assign_operators:
            self.possible_types[op][INT][INT] = INT
            self.possible_types[op][FLOAT][FLOAT] = FLOAT
            self.possible_types[op][INT][FLOAT] = FLOAT
            self.possible_types[op][FLOAT][INT] = FLOAT

        for op in dot_operators:
            self.possible_types[op][VECTOR][VECTOR] = VECTOR
            self.possible_types[op][VECTOR][INT] = VECTOR
            self.possible_types[op][INT][VECTOR] = VECTOR
            self.possible_types[op][FLOAT][VECTOR] = VECTOR
            self.possible_types[op][VECTOR][FLOAT] = VECTOR
            self.possible_types[op][MATRIX][MATRIX] = VECTOR
            self.possible_types[op][MATRIX][INT] = VECTOR
            self.possible_types[op][MATRIX][FLOAT] = VECTOR
            self.possible_types[op][INT][MATRIX] = VECTOR
            self.possible_types[op][FLOAT][MATRIX] = VECTOR

        for op in comparison_operators:
            self.possible_types[op][INT][INT] = BOOL
            self.possible_types[op][FLOAT][INT] = BOOL
            self.possible_types[op][INT][FLOAT] = BOOL
            self.possible_types[op][FLOAT][FLOAT] = BOOL

        self.possible_types['+'][STRING][STRING] = STRING
        self.possible_types['*'][STRING][INT] = STRING
        self.possible_types['*'][INT][STRING] = STRING
        self.possible_types['+='][STRING][STRING] = STRING

    def get_result_type(self, op, left, right):
        if op in self.possible_types and left.type in self.possible_types[op] \
                and right.type in self.possible_types[op][left.type]:
            return self.possible_types[op][left.type][right.type]
        return None

    def check_dimensions(self, op, left, right):
        if op == '=':
            return right.dimensions
        if op in ['+', '-','-=', '+='] + dot_operators + assign_operators:
            if left.dimensions == right.dimensions:
                return left.dimensions
        if op =='*':
            if left.dimensions[1] == right.dimensions[0]:
                return [left.dimensions[0], right.dimensions[1]]
        if op == '/':
            return [left.dimensions[0], right.dimensions[1]]
        return None


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        print("Gen visit: " + node.__class__.__name__ + ": " + str(node))
    #    if isinstance(node, list):
    #        for elem in node:
    #            self.visit(elem)
    #    elif node is not None:
    #        for child in node.children:
    #            if isinstance(child, list):
    #                for item in child:
    #                    if isinstance(item, AST.Node):
    #                        self.visit(item)
    #            elif isinstance(child, AST.Node):
    #                self.visit(child)


class TypeChecker(NodeVisitor):
    def __init__(self):
        self.table = SymbolTable(None, 'Program')
        self.operations = Operations()
        self.loop_iterator = 0

    def visit_Program(self, node):
        self.visit(node.instructions)

    def visit_Instructions(self, node):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_Instruction(self, node):
        self.visit(node.instruction)

    def visit_If(self, node):
        self.visit(node.condition)
        self.visit(node.instruction)

    def visit_IfElse(self, node):
        self.visit(node.condition)
        self.visit(node.if_instruction)
        self.visit(node.else_instruction)

    def visit_For(self, node):
        self.visit(node.id)
        self.visit(node.start_loop)
        self.visit(node.stop_loop)
        self.loop_iterator += 1
        self.visit(node.instruction)
        self.loop_iterator -= 1

    def visit_While(self, node):
        self.visit(node.condition)
        self.loop_iterator += 1
        self.visit(node.instruction)
        self.loop_iterator -= 1

    def visit_Assign(self, node):
        l_value = self.visit(node.l_value)
        op = node.operator
        r_value = self.visit(node.expression)
        _type = self.operations.get_result_type(op, l_value, r_value)
        if _type is not None:
            if _type is MATRIX:
                dimensions = self.operations.check_dimensions(op, l_value, r_value)
                if dimensions is not None:
                    print("Array assignment" + l_value + op + r_value)
                    self.table.put(l_value.name, ArraySymbol(l_value.name, r_value.dimensions))
                else:
                    print("Wrong Array assignment" + l_value + op + r_value)
            else:
                print("Variable Assignment" + l_value + op + r_value)
                self.table.put(l_value.name, VariableSymbol(l_value.name, r_value.type))
        elif isinstance(l_value, VariableSymbol) and isinstance(r_value, ArraySymbol):
            new_l = ArraySymbol(l_value.name, r_value.dimensions)
            self.table.put(l_value.name, new_l)
        elif isinstance(l_value, VariableSymbol):
            l_value.type = r_value.type
        else:
            print("Wrong Assignment" + str(l_value) + op + str(r_value))

    def visit_Expressions(self, node):
        if node.expressions is not None:
            for expr in node.expressions:
                self.visit(expr)

    def visit_Break(self, node):
        if not self.loop_iterator > 0:
            print("BREAK outside loop function")

    def visit_Continue(self, node):
        if not self.loop_iterator > 0:
            print("CONTINUE outside loop function")

    def visit_Return(self, node):
        if node.expressions is not None:
            self.visit(node.expressions)

    def visit_Print(self, node):
        if node.expressions is not None:
            self.visit(node.expressions)

    def visit_Variable(self, node):
        var = self.table.get(node.name)
        if var is None:
            new_var = VariableSymbol(node.name, None)
            self.table.put(node.name, new_var)
            return new_var
        else:
            return var

    def visit_Reference(self, node):
        var = self.table.get(node.name)
        self.visit(node.indexes)
        if var is None:
            print("Unknown reference to {}".format(node.name))
        else:
            dimensions = var.dimensions
            if len(node.indexes.indexes) > len(dimensions):
                print("Dimensions out of bounds at {}".format(node.name))
            for i, index in enumerate(node.indexes.indexes):
                if index.value > dimensions[i]:
                    print("Index out of bounds: {0}, dimension limit: {1}".format(index.value, dimensions[i]))
        return VariableSymbol(None, None)

    def visit_Indexes(self, node):
        for index in node.indexes:
            _type = self.visit(index)
            if _type.type != INT:
                print("Index error, type not int: {}".format(_type))
                return _type
        return INT

    def visit_Condition(self, node):
        left = self.visit(node.left)
        op = node.operator
        right = self.visit(node.right)
        _type = self.operations.get_result_type(op, left, right)

        if _type != BOOL:
            print("Wrong condition: {0) {1} {2} ".format(left, op, right))

    def visit_Integer(self, node):
        return VariableSymbol(None, INT)

    def visit_Float(self, node):
        return VariableSymbol(None,  FLOAT)

    def visit_String(self, node):
        return VariableSymbol(None, STRING)

    def visit_Matrix(self, node):
        vector_lengths = [len(v.numbers) for v in node.vectors]
        vector_no = len(node.vectors)
        if len(set(vector_lengths)) != 1:
            print("Wrong Vector sizes, must be of same length in one matrix")

        return ArraySymbol(None, [vector_no, vector_lengths.pop()])

    def visit_Vector(self, node):
        _types = set()
        vector_length = 0
        for number in node.numbers:
            _type = self.visit(number)
            _types.add(_type.type)
            vector_length += 1
            if _type.type not in [INT, FLOAT]:
                print("Wrong Vector values! they can only by Int or Float, got: {}".format(_type))
            if len(_types) != 1:
                print("Wrong Vector types with more than one type: {}".format(_types))
        return ArraySymbol(None, [vector_length])

    def visit_BinaryExpression(self, node):
        left = self.visit(node.left)
        op = node.operator
        right = self.visit(node.right)

        _type = self.operations.get_result_type(op, left, right)
        if _type is MATRIX:
            dims = self.operations.check_dimensions(op. left, right)
            if dims is None:
                print("Wrong dimensions in binary expression: {0} {1} {2}".format(str(left), op, str(right)))
                return ArraySymbol(None, None)
            else:
                return ArraySymbol(None, dims)
        elif _type is None:
            print("Wrong Binary Expression: {0} {1} {2}".format(str(left), op, str(right)))
        return VariableSymbol(None, _type)

    def visit_UnaryNegation(self, node):
        _type = self.visit(node.expression)
        op = node.operator
        if _type not in[INT, FLOAT]:
            print("Wrong Unary Negation " + op + _type)
        return _type

    def visit_Transposition(self, node):
        _type = self.visit(node.expression)
        if _type != ArraySymbol.__class__:
            print("Wrong Transposition, it only works with matrices: " + _type)

    def  visit_MatrixFunctions(self, node):
        _type = self.visit(node.expression)
        if _type.type is not INT:
            print("Matrix function's argument must be INT")

        return ArraySymbol(None, [node.expression.value, node.expression.value])

    def get_symbol_table(self):
        return self.table



