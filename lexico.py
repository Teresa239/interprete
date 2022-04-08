#Analizador lexico
#Alumnos: 
# Guerra Gonzalez Alan Ricardo
# Meraz Hernandez Brian Alexis
# Santos Rodriguez Maria Teresa

import ply.lex as lex

tokens  = (
    'REVALUAR',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'DECIMAL',
    'LETRAMINUS',
    'LETRAMAYUS',
    'ENTERO',
    'PTCOMA',
    'PUNTO',
    'ASIGNAR',
    'MODULO',

    #Logica
    'AND',
    'OR', 
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
)

reservada = {
    'include' : 'INCLUDE',
    'using' : 'USING',
    'namespace' : 'NAMESPACE',
    'std' : 'STD',
    'count' : 'COUNT',
    'cin': 'CIN',
    'get' : 'GET',
    'cadena' : 'CADENA',
    'retunr' : 'RETURN',
    'void' : 'VOID',
    'int' : 'INT',
    'endl' : 'ENDL',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
}
 # Expresiones regulares de los tokens - Contexto simple

# Tokens
t_REVALUAR  = r'Evaluar'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORIZQ    = r'\['
t_CORDER    = r'\]'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PTCOMA    = r';'
t_LETRAMINUS = r'[a-z]'
t_LETRAMAYUS = r'[A-Z]'
t_PUNTO     = r'.'
t_ASIGNAR   = r'='
t_MODULO    = r'\%'

t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal muy largo %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero muy largo %d", t.value)
        t.value = 0
    return t

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador léxico
lexer = lex.lex()

data = input("Ingrese: ")

# Input del lexer
lexer.input(data)

print('----------------------ANALIZADOR LEXICO-----------------: ')

# Token
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)


############ CADENAS ACEPTADAS ###################
#Evaluar[1+1];
#Evaluar[1+1*2];
#Evaluar[-(1+1*6/3-5+7)];
#Evaluar[-(1+1*6/3-5+1*-2)];
#Evaluar[-(1.6+1.45)];