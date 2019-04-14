

class Node(object):
    pass


class Program(Node):
    def __init__(self, instructions=None):
        self.instructions = instructions


class Instructions(Node):
    def __init__(self, instruction):
        self.instructions = [instruction]

    def add_instruction(self, instruction):
        self.instructions.append(instruction)


class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction


class If(Node):
    def __init__(self, condition, instruction):
        self._if = "IF"
        self.condition = condition
        self.then = "THEN"
        self.instruction = instruction


class IfElse(Node):
    def __init__(self, condition, if_instruction, else_instruction):
        self._if = "IF"
        self.condition = condition
        self.then = "THEN"
        self.if_instruction = if_instruction
        self._else = "ELSE"
        self.else_instruction = else_instruction


class For(Node):
    def __init__(self, id, start_loop, stop_loop, instruction):
        self._for = "FOR"
        self.id = id
        self.range = "RANGE"
        self.start_loop = start_loop
        self.stop_loop = stop_loop
        self.instruction = instruction


class While(Node):
    def __init__(self, condition, instruction):
        self._while = "WHILE"
        self.condition = condition
        self.instruction = instruction


class Assign(Node):
    def __init__(self, l_value, operator, expression):
        self.l_value = l_value
        self.operator = operator
        self.expression = expression


class Expressions(Node):
    def __init__(self, expression):
        self.expressions = [expression]

    def add_expression(self, expression):
        self.expressions.append(expression)


class Break(Node):
    def __init__(self):
        self._break = "BREAK"


class Continue(Node):
    def __init__(self):
        self._continue = "CONTINUE"


class Return(Node):
    def __init__(self, expressions):
        self._break = "BREAK"
        self.expressions = expressions


class Print(Node):
    def __init__(self, expressions):
        self._print = "PRINT"
        self.expressions = expressions


class Variable(Node):
    def __init__(self, name):
        self.name = name


class Reference(Node):
    def __init__(self, name, indexes):
        self.reference = "REF"
        self.name = name
        self.indexes = indexes


class Indexes(Node):
    def __init__(self, index):
        self.indexes = [index]

    def add_index(self, index):
        self.indexes.append(index)


class Condition(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Integer(Node):
    def __init__(self, value):
        self.value = value


class Float(Node):
    def __init__(self, value):
        self.value = value


class String(Node):
    def __init__(self, name):
        self.name = name


class Matrix(Node):
    def __init__(self, vector):
        self.vector = "VECTOR"
        self.vectors = [vector]

    def add_vector(self, vector):
        self.vectors.append(vector)


class Vector(Node):
    def __init__(self, number):
        self.vector = "VECTOR"
        self.numbers = [number]

    def add_number(self, number):
        self.numbers.append(number)


class BinaryExpression(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class UnaryNegation(Node):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression


class Transposition(Node):
    def __init__(self, expression):
        self.transpose = "TRANSPOSE"
        self.expression = expression


class MatrixFunctions(Node):
    def __init__(self, function, expression):
        self.function = function
        self.expression = expression


class Error(Node):
    def __init__(self):
        pass
