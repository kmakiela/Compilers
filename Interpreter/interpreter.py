
from SyntaxTree import AST
from Interpreter.Memory import *
from Interpreter.Exceptions import *
from Interpreter.visit import *
import sys
import numpy as np

sys.setrecursionlimit(10000)


class OperatorFunctions(object):
    def __init__(self):
        self.functions = {
            '+': (lambda x, y: x + y),
            '+=': (lambda x, y: x + y),
            '-': (lambda x, y: x - y),
            '-=': (lambda x, y: x - y),
            '*': (lambda x, y: x * y),
            '*=': (lambda x, y: x * y),
            '/': (lambda x, y: x / y),
            '/=': (lambda x, y: x / y),

            '==': (lambda x, y: x == y),
            '!=': (lambda x, y: x != y),
            '>=': (lambda x, y: x >= y),
            '>': (lambda x, y: x > y),
            '<=': (lambda x, y: x <= y),
            '<': (lambda x, y: x < y),

            '.+': (lambda x, y: (np.matrix(x) + np.matrix(y)).tolist()),
            '.-': (lambda x, y: (np.matrix(x) - np.matrix(y)).tolist()),
            '.*': (lambda x, y: np.multiply(np.array(x), np.array(y)).tolist()),
            './': (lambda x, y: np.divide(np.array(x), np.array(y)).tolist())
        }


class Interpreter(object):
    def __init__(self):
        self.operations = OperatorFunctions()
        self.memory_stack = MemoryStack()

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Program)
    def visit(self, node):
        node.instructions.accept(self)

    @when(AST.Instructions)
    def visit(self, node):
        self.memory_stack.push(Memory("instruction block"))
        for instruction in node.instructions:
            instruction.accept(self)
        self.memory_stack.pop()

    @when(AST.Instruction)
    def visit(self, node):
        node.instruction.accept(self)

    @when(AST.If)
    def visit(self, node):
        node.condition.accept(self)
        node.instruction.accept(self)

    @when(AST.IfElse)
    def visit(self, node):
        node.condition.accept(self)
        node.if_instruction.accept(self)
        node.else_instruction.accept(self)

    @when(AST.For)
    def visit(self, node):
        start_loop = node.start_loop.accept(self)
        stop_loop = node.stop_loop.accept(self)
        iterator = node.id.accept(self)

        self.memory_stack.set(node.id.name, start_loop)
        while iterator < stop_loop:
            try:
                node.instruction.accept(self)
            except BreakException:
                break
            except ContinueException:
                continue
            iterator = node.id.accept(self) + 1
            self.memory_stack.set(node.id.name, iterator)

    @when(AST.While)
    def visit(self, node):
        while node.condition.accept(self):
            try:
                node.instruction.accept(self)
            except BreakException:
                break
            except ContinueException:
                continue

    @when(AST.Assign)
    def visit(self, node):
        r_value = node.expression.accept(self)
        if node.operator == '=':
            if isinstance(node.l_value, AST.Reference):
                tmp = np.array(self.memory_stack.get(node.l_value.name))
                indexes = tuple([i.accept(self) for i in node.l_value.indexes.indexes])
                tmp[indexes] = r_value
                self.memory_stack.set(node.l_value.name, tmp.tolist())
            else:
                self.memory_stack.set(node.l_value.name, r_value)
        else:
            l_value = self.memory_stack.get(node.l_value.name)
            result = self.operations.functions[node.operator](l_value, r_value)
            self.memory_stack.set(node.l_value.name, result)

    @when(AST.Expressions)
    def visit(self, node):
        return [expr.accept(self) for expr in node.expressions]
        # for expression in node.expressions:
        #    expression.accept(self)

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()

    @when(AST.Return)
    def visit(self, node):
        # TODO something more here?
        for expression in node.expressions:
            expression.accept(self)

    @when(AST.Print)
    def visit(self, node):
        for expr in node.expressions.accept(self):
            print(expr, end=" ")
        print("\n")

    @when(AST.Variable)
    def visit(self, node):
        return self.memory_stack.get(node.name)

    @when(AST.Reference)
    def visit(self, node):
        array = np.array(self.memory_stack.get(node.name))
        indexes = tuple([i.accept(self) for i in node.indexes.indexes])
        if isinstance(array[indexes], np.ndarray):
            return array[indexes].tolist()
        else:
            return array[indexes]

    @when(AST.Condition)
    def visit(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        return self.operations.functions[node.operator](left, right)

    @when(AST.Integer)
    def visit(self, node):
        return node.value

    @when(AST.Float)
    def visit(self, node):
        return node.value

    @when(AST.String)
    def visit(self, node):
        return node.name[1:-1]

    @when(AST.Matrix)
    def visit(self, node):
        return [v.accept(self) for v in node.vectors]

    @when(AST.Vector)
    def visit(self, node):
        return [n.accept(self) for n in node.numbers]

    @when(AST.BinaryExpression)
    def visit(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)

        return self.operations.functions[node.operator](left, right)

    @when(AST.UnaryNegation)
    def visit(self, node):
        expr = node.expression.accept(self)
        return -expr

    @when(AST.Transposition)
    def visit(self, node):
        return np.transpose(node.expression.accept(self)).tolist()

    @when(AST.MatrixFunctions)
    def visit(self, node):
        expression = node.expression.accept(self)
        if node.function == 'zeros':
            return np.zeros(expression).tolist()
        elif node.function == 'ones':
            return np.ones(expression).tolist()
        elif node.function == 'eye':
            return np.eye(expression).tolist()


