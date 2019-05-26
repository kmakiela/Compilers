#!/usr/bin/python

import Skaner.scanner as scanner
import ply.yacc as yacc
import SyntaxTree.AST as AST

lexer = scanner.lexer
tokens = scanner.tokens

precedence = (
   ('nonassoc', 'IF_NO_ELSE'),
   ('nonassoc', 'ELSE'),
   ('right', 'ASSIGN', 'PLUSASSIGN', 'MINUSASSIGN', 'TIMESASSIGN', 'DIVIDEASSIGN'),
   ('left', 'EQ', 'LT', 'GT', 'LQ', 'GQ', 'NE'),
   ("left", '+', '-', 'DOTPLUS', 'DOTMINUS'),
   ('left', '*', '/', 'DOTTIMES', 'DOTDIVIDE'),
   ('right', 'UNARY_NEGATION'),
   ('left', 'TRANSPOSITION')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}, lexpos {1}: LexToken({2}, '{3}')".format(p.lineno, p.lexpos, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions
        | """
    if len(p) == 2:
        p[0] = AST.Program(p[1])
    else:
        p[0] = AST.Program()


def p_instructions_1(p):
    """instructions : instructions instruction """
    p[0] = p[1]
    p[0].add_instruction(p[2])


def p_instructions_2(p):
    """instructions : instruction """
    p[0] = AST.Instructions(p[1])


def p_instruction_if(p):
    """instruction : IF '(' condition ')' instruction %prec IF_NO_ELSE"""
    p[0] = AST.If(p[3], p[5])
    

def p_instruction_if_else(p):
    """instruction : IF '(' condition ')' instruction ELSE instruction"""
    p[0] = AST.IfElse(p[3], p[5], p[7])


def p_instruction_for(p):
    """instruction : FOR ID ASSIGN expression ':' expression instruction"""
    p[0] = AST.For(AST.Variable(p[2]), p[4], p[6], p[7])


def p_instruction_while(p):
    """instruction : WHILE '(' condition ')' instruction"""
    p[0] = AST.While(p[3], p[5])


def p_instruction_block(p):
    """instruction : '{' instructions '}'"""
    p[0] = p[2]


def p_instruction_semicolon(p):
    """instruction : one_line_instruction ';'"""
    p[0] = p[1]


def p_assign(p):
    """one_line_instruction : left_value ASSIGN expression
        | left_value PLUSASSIGN expression
        | left_value MINUSASSIGN expression
        | left_value TIMESASSIGN expression
        | left_value DIVIDEASSIGN expression"""
    p[0] = AST.Assign(p[1], p[2], p[3], p.lineno(2))


def p_instruction_return(p):
    """one_line_instruction : RETURN expressions"""
    p[0] = AST.Return(p[2])


def p_instruction_break(p):
    """one_line_instruction : BREAK"""
    p[0] = AST.Break(p.lineno(1))


def p_instruction_print(p):
    """one_line_instruction : PRINT expressions"""
    p[0] = AST.Print(p[2])


def p_instruction_continue(p):
    """one_line_instruction : CONTINUE"""
    p[0] = AST.Continue(p.lineno(1))


def p_expressions(p):
    """expressions : expressions ',' expression
        | expression"""
    if len(p) == 4:
        p[0] = p[1]
        p[0].add_expression(p[3])
    else:
        p[0] = AST.Expressions(p[1])


def p_left_value_expr(p):
    """expression : left_value"""
    p[0] = p[1]


def p_left_value_id(p):
    """left_value : ID"""
    p[0] = AST.Variable(p[1])


def p_left_value_matrix(p):
    """left_value : matrix_id"""
    p[0] = p[1]


def p_matrix_id(p):
    """matrix_id : ID '[' indexes ']'"""
    p[0] = AST.Reference(p[1], p[3], p.lineno(2))


def p_indexes(p):
    """indexes : indexes ',' ID
        | indexes ',' INTEGER
        | INTEGER
        | ID"""
    def check_type(elem):
        return AST.Integer(elem) if isinstance(elem, int) else elem
    if len(p) == 4:
        p[0] = p[1]
        p[0].add_index(check_type(p[3]))
    else:
        p[0] = AST.Indexes(check_type(p[1]))


def p_condition(p):
    """condition : expression EQ expression
        | expression LT expression
        | expression GT expression
        | expression LQ expression
        | expression GQ expression
        | expression NE expression"""
    p[0] = AST.Condition(p[1], p[2], p[3])


def p_expression_int(p):
    """expression : INTEGER"""
    p[0] = AST.Integer(p[1])


def p_expression_float(p):
    """expression : FLOAT"""
    p[0] = AST.Float(p[1])


def p_expression_string(p):
    """expression : STRING"""
    p[0] = AST.String(p[1])


def p_expression_matrix(p):
    """expression : matrix"""
    p[0] = p[1]


def p_matrix(p):
    """matrix : '[' vectors ']'
        | '[' matrix_elements ']'"""
    p[0] = p[2]


def p_vectors(p):
    """vectors : vectors ',' vector
        | vector"""
    if len(p) == 4:
        p[0] = p[1]
        p[0].add_vector(p[3])
    else:
        p[0] = AST.Matrix(p[1], p.lineno(1))


def p_vector(p):
    """vector : '[' matrix_elements ']' """
    p[0] = p[2]


def p_matrix_elements(p):
    """matrix_elements : matrix_elements ',' ID
        | matrix_elements ',' FLOAT
        | matrix_elements ',' INTEGER
        | ID
        | INTEGER
        | FLOAT"""
    def check_type(elem):
        return AST.Integer(elem) if isinstance(elem, int) else AST.Float(elem) if isinstance(elem, float) else elem

    if len(p) == 4:
        p[0] = p[1]
        p[0].add_number(check_type(p[3]))
    elif len(p) == 2:
        p[0] = AST.Vector(check_type(p[1]), p.lineno(1))


def p_operators(p):
    """expression : expression '+' expression
        | expression '-' expression
        | expression '*' expression
        | expression '/' expression"""
    p[0] = AST.BinaryExpression(p[1], p[2], p[3], p.lineno(2))


def p_dot_operators(p):
    """expression : expression DOTPLUS expression
        | expression DOTMINUS expression
        | expression DOTTIMES expression
        | expression DOTDIVIDE expression"""
    p[0] = AST.BinaryExpression(p[1], p[2], p[3], p.lineno(2))


def p_array_functions(p):
    """expression : ZEROS '(' expression ')'
        | ONES '(' expression ')'
        | EYE '(' expression ')'"""
    p[0] = AST.MatrixFunctions(p[1], p[3], p.lineno(1))


def p_unary_negation(p):
    """expression : '-' expression %prec UNARY_NEGATION"""
    p[0] = AST.UnaryNegation(p[1], p[2])


def p_transposition(p):
    """expression : expression TRANSPOSITION"""
    p[0] = AST.Transposition(p[1])

parser = yacc.yacc()

