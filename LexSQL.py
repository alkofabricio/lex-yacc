# Configuracao dos Tokens


reserved = { # Estas sao as palavras reservadas
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
}

tokens = ['ID', 'ASTERISCO', 'EQ'] + list(reserved.values())


# Este metodo faz o tratamento nao reconhecer as palavras reservadas como ID
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


# Este metodo percorre as regras definidas abaixo
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Este e o tipo de token que sera ignorado
t_ignore = ' \t'

t_ASTERISCO = r'\*'
t_EQ = r'\='


def t_error(t):
    raise TypeError("Texto desconhecido %s" % (t.type))

# Instanciando o lexer
import ply.lex as lex
lexer = lex.lex()


# Regras de precedendia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ'),
)


""" A gramatica usada neste analisador

I -> sCfAwD
C -> A | *
D -> D and D | D or D | E
E -> A = A
A -> id

Nao terminais:
    inicial     - I
    column      - C
    condition   - D
    expressao   - E
    atom        - A

Terminais:
    SELECT      - s
    FROM        - f
    WHERE       - w 
    ASTERISCO   - *
    ID          - id
    AND         - and
    OR          - or
    EQ          - =

"""


def p_inicial(t):
    # select * from tabela where name=name and name=name
    '''
    inicial : SELECT column FROM atom WHERE condition
    '''
    t[0] = ('select', t[2], 'from', t[4], 'where', t[6])
    print("Sintaxe Correta")


def p_column(t):
    '''
     column : atom
            | ASTERISCO
    '''
    t[0] = t[1]


def p_condition(t):
    '''
    condition : condition AND condition
              | condition OR condition
              | expressao

    '''
    if len(t) == 4:
        t[0] = t[1], t[2], t[3]
    elif len(t) == 2:
        t[0] = t[1]

def p_expressao(t):
    '''
    expressao : atom EQ atom
    '''
    t[0] = (t[1], t[2], t[3])


def p_atom(t):
    '''
    atom : ID
    '''
    t[0] = t[1]

def p_error(t):
    if t:
        print ("Erro sintatico em ",  t.value)
    else:
        print "Erro sintatico no EOF"

# Configurando o YACC
import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = raw_input("Digite a sentenca: ")
    except EOFError:
        break
    parser.parse(s)


