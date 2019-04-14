from __future__ import print_function
import SyntaxTree.AST as AST


def addToClass(cls):

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Node)
    def print_indented(self, content, indent=0):
        print(indent * "| " + content)

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        self.instructions.printTree(indent)

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        if self.instructions:
            for instruction in self.instructions:
                instruction.printTree(indent)

    @addToClass(AST.If)
    def printTree(self, indent=0):
        self.print_indented(self._if, indent)
        self.condition.printTree(indent + 1)
        self.print_indented(self._then, indent)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.IfElse)
    def printTree(self, indent=0):
        self.print_indented(self._if, indent)
        self.condition.printTree(indent + 1)
        self.print_indented(self._then, indent)
        self.if_instruction.printTree(indent + 1)
        self.print_indented(self._else, indent)
        self.else_instruction.printTree(indent + 1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        self.print_indented(self._for, indent)
        self.print_indented(self.id, indent + 1)
        self.print_indented(self.range, indent + 1)
        self.print_indented(str(self.start_loop), indent + 2)
        self.print_indented(str(self.stop_loop), indent + 2)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        self.print_indented(self._while, indent)
        self.condition.printTree(indent + 1)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Assign)
    def printTree(self, indent=0):
        self.print_indented(self.operator, indent)
        self.l_value.printTree(indent + 1)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        self.print_indented(self._break, indent)

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        self.print_indented(self._continue, indent)

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        self.print_indented(self._return, indent)
        for expr in self.expressions.elems:
            expr.printTree(indent + 1)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        self.print_indented(self._print, indent)
        for expr in self.expressions.elems:
            expr.printTree(indent + 1)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        self.print_indented(self.name, indent)

    @addToClass(AST.Reference)
    def printTree(self, indent=0):
        self.print_indented(self.reference, indent)
        self.print_indented(self.name, indent + 1)
        self.indexes.printTree(indent + 1)

    @addToClass(AST.Indexes)
    def printTree(self, indent=0):
        for index in self.indexes:
            index.printTree(indent + 1)

    @addToClass(AST.Condition)
    def printTree(self, indent=0):
        self.print_indented(self.operator, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Integer)
    def printTree(self, indent=0):
        self.print_indented(str(self.value), indent)

    @addToClass(AST.Float)
    def printTree(self, indent=0):
        self.print_indented(str(self.value), indent)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        self.print_indented(self.name, indent)

    @addToClass(AST.Matrix)
    def printTree(self, indent=0):
        self.print_indented(self.vector, indent)
        for v in self.vectors:
            v.printTree(indent + 1)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        self.print_indented(self.vector, indent)
        for n in self.numbers:
            n.printTree(indent + 1)

    @addToClass(AST.BinaryExpression)
    def printTree(self, indent=0):
        self.print_indented(self.operator, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.UnaryNegation)
    def printTree(self, indent=0):
        self.print_indented(self.operator, indent)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Transposition)
    def printTree(self, indent=0):
        self.print_indented(self.transpose, indent)
        self.expression.printTree(indent + 1)

    @addToClass(AST.MatrixFunctions)
    def printTree(self, indent=0):
        self.print_indented(self.function, indent)
        self.expression.printTree(indent + 1)
