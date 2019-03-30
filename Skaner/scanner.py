#!/usr/bin/python

import sys
import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT'
}

tokens = [
    'DOTPLUS',
    'DOTMINUS',
    'DOTTIMES',
    'DOTDIVIDE',  # functions

    'ASSIGN',
    'PLUSASSIGN',
    'MINUSASSIGN',
    'TIMESASSIGN',
    'DIVIDEASSIGN',  # functions

    'EQ',
    'LT',
    'GT',
    'LQ',
    'GQ',
    'NE',

    'TRANSPOSITION',  # literals

    'ID',
    'INTEGER',
    'FLOAT',
    'STRING'  # functions
] + list(reserved.values())

literals = "+-*/:,;()[]{}"

t_TRANSPOSITION = r'\''
t_ignore = ' \t'


def t_FLOAT(t):
    r'(\d*\.\d+|\d+\.\d*)([Ee][+-]?\d*)?'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = str(t.value)
    return t


def t_DOTPLUS(t):
    r'\.\+'
    t.value = ".+"
    return t


def t_DOTMINUS(t):
    r'\.\-'
    t.value = ".-"
    return t


def t_DOTTIMES(t):
    r'\.\*'
    t.value = ".*"
    return t


def t_DOTDIVIDE(t):
    r'\.\/'
    t.value = "./"
    return t


def t_GQ(t):
    r'>='
    t.value = ">="
    return t


def t_LQ(t):
    r'<='
    t.value = "<="
    return t

def t_EQ(t):
    r'=='
    t.value = "=="
    return t


def t_LT(t):
    r'<'
    t.value = "<"
    return t


def t_GT(t):
    r'>'
    t.value = ">"
    return t


def t_NE(t):
    r'!='
    t.value = "!="
    return t


def t_ASSIGN(t):
    r'='
    t.value = "="
    return t


def t_PLUSASSIGN(t):
    r'\+='
    t.value = "+="
    return t


def t_MINUSASSIGN(t):
    r'\-='
    t.value = "-="
    return t


def t_TIMESASSIGN(t):
    r'\*='
    t.value = "*="
    return t


def t_DIVIDEASSIGN(t):
    r'\/='
    t.value = "/="
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_error(t):
    print("line %d: illegal character '%s'" %(t.lineno, t.value[0]) )
    t.lexer.skip(1)


lexer = lex.lex()
fh = None


