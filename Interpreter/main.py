
import sys
import ply.yacc as yacc
from Parser import Mparser
from SyntaxTree import TreePrinter
from SemanticsCheck.TypeChecker import TypeChecker
from Interpreter import interpreter
from Skaner import scanner


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    # in future
    # ast.accept(OptimizationPass1())
    # ast.accept(OptimizationPass2())
    # ast.accept(CodeGenerator())

    parser = yacc.yacc(module=Mparser)
    text = file.read()

    ast = parser.parse(text, lexer=scanner.lexer)
    # ast.printTree()

    typeChecker = TypeChecker()
    typeChecker.visit(ast)
    # Interpreter().visit(ast)
    ast.accept(interpreter.Interpreter())
