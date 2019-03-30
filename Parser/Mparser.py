#!/usr/bin/python

import Skaner.scanner as scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
   ('nonassoc', 'RETURN'),
   ('nonassoc', 'IF_NO_ELSE'),
   ('nonassoc', 'ELSE'),
   ('nonassoc', 'ID'),
   ('nonassoc', 'PRINT'),
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
    """program : instructions_opt"""


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction """


def p_instructions_2(p):
    """instructions : instruction """


def p_instruction_if(p):
    """instruction : IF '(' condition ')' instruction %prec IF_NO_ELSE"""
    

def p_instruction_if_else(p):
    """instruction : IF '(' condition ')' instruction ELSE instruction"""


def p_instruction_for(p):
    """instruction : FOR ID ASSIGN expression ':' expression instruction"""


def p_instruction_while(p):
    """instruction : WHILE '(' condition ')' instruction"""


def p_instruction_block(p):
    """instruction : '{' instructions '}'"""


def p_instruction_semicolon(p):
    """instruction : one_line_instruction ';'"""


def p_assign(p):
    """one_line_instruction : left_value ASSIGN expression
        | left_value PLUSASSIGN expression
        | left_value MINUSASSIGN expression
        | left_value TIMESASSIGN expression
        | left_value DIVIDEASSIGN expression"""


def p_keywords(p):
    """one_line_instruction : BREAK
        | CONTINUE
        | RETURN expressions
        | PRINT expressions"""


def p_expressions(p):
    """expressions : expressions ',' expression
        | expression"""


def p_left_value(p):
    """expression : left_value
        left_value : ID
            | matrix_id"""


def p_matrix_id(p):
    """matrix_id : ID '[' indexes ']'"""


def p_indexes(p):
    """indexes : indexes ',' index
        | index
        | index ':' index"""


def p_index(p):
    """index : ID
        | INTEGER"""


def p_condition(p):
    """condition : expression EQ expression
        | expression LT expression
        | expression GT expression
        | expression LQ expression
        | expression GQ expression
        | expression NE expression"""


def p_expression(p):
    """expression : INTEGER
        | FLOAT
        | STRING
        | matrix"""


def p_matrix(p):
    """matrix : '[' matrices ']'
        | '[' vectors ']'"""


def p_matrices(p):
    """matrices : matrices ',' matrix
        | matrix"""


def p_vectors(p):
    """vectors : vectors ';' matrix_elements
        | matrix_elements"""


def p_matrix_elements(p):
    """matrix_elements : matrix_elements ',' index
        | matrix_elements ',' FLOAT
        | index
        | FLOAT"""


def p_operators(p):
    """expression : expression '+' expression
        | expression '-' expression
        | expression '*' expression
        | expression '/' expression"""


def p_dot_operators(p):
    """expression : expression DOTPLUS expression
        | expression DOTMINUS expression
        | expression DOTTIMES expression
        | expression DOTDIVIDE expression"""


def p_array_functions(p):
    """expression : ZEROS '(' expression ')'
        | ONES '(' expression ')'
        | EYE '(' expression ')'"""


def p_unary_negation(p):
    """expression : '-' expression %prec UNARY_NEGATION"""


def p_transposition(p):
    """expression : expression TRANSPOSITION"""


parser = yacc.yacc()

