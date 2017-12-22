import ply.lex as lex

tokens = ['ID', 'ASTERISCO', 'EQ', 'nEQ', 'VIRG']

reserved = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
}

tokens += list(reserved.values())

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


t_ASTERISCO = r'\*'
t_VIRG = r'\,'
t_EQ = r'\='

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print('Caractere invalido = %s' % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = raw_input("Digite a sentenca: ")

lexer.input(data.lower())

resultado = []
cont = 0

while True:
    ltoken = lexer.token()
    if not ltoken:
        cont = 0
        break
    #print(ltoken.value, ltoken.type) # Print para proposito de teste
    resultado.append(ltoken.type)
    cont += 1

if len(resultado) == 8:
    if (resultado[0] == 'SELECT' and
            (resultado[1] == 'ID' or resultado[1] == 'ASTERISCO')
            and resultado[2] == 'FROM'
            and resultado[3] == 'ID'
            and resultado[4] == 'WHERE'
            and resultado[5] == 'ID'
            and resultado[6] == 'EQ'
            and resultado[7] == 'ID'):

        print ("Sintaxe correta")
    else:
        print("Error de sintaxe!")


elif len(resultado) == 12:
    if (resultado[0] == 'SELECT' and
            (resultado[1] == 'ID' or resultado[1] == 'ASTERISCO')
            and resultado[2] == 'FROM'
            and resultado[3] == 'ID'
            and resultado[4] == 'WHERE'
            and resultado[5] == 'ID'
            and resultado[6] == 'EQ'
            and resultado[7] == 'ID'
            and (resultado[8] == 'AND' or resultado[8] == 'OR')
            and resultado[9] == 'ID'
            and resultado[10] == 'EQ'
            and resultado[11] == 'ID'):

        print ("Sintaxe correta\n")
    else:
        print("Error de sintaxe!")

else:
    print("Error de sintaxe!")


