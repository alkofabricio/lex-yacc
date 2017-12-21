// Analisador de comandos SQL
%{
    #include <stdio.h>

    int yylex(void);

    int yywrap(){
        return 1;
    }

    void yyerror(const char *erro){
        fprintf(stderr, "Ocorreu um erro: %s\n", erro);
    }
  
%}

//Neste bloco, sera feita a construcao logica da analise dos comandos que foram mapeados.
%%
%token SELECT FROM IDENTIFIER WHERE OR AND;

//Ele verifica a linha que foi enviada e cada palavra que compoe esta linha estao definidas abaixo
//Quando ele detecta a sintaxe como correta, o programa encerra.
line: selecionar itens usando condicao '\n'{
    printf("Sintaxe Correcta\n");
    return 0;
};

/* Gramatica da logica usada
Sendo os terminais
    line = L (Inicial)
    selecionar = S
    itens = I
    identificadores = D
    usando = U
    condicao = C
    
Os nao terminais:
    SELECT = s
    IDENTIFIER = id
    AND = a
    OR = o

Podemos escrever a logica de analise assim:
        L -> SIUC
        S -> s
        I -> * | D
        D -> id | id,D
        C -> D=D | D=DaC | D=DoC
*/

selecionar: SELECT;

itens: '*' | identificadores;

identificadores: IDENTIFIER | IDENTIFIER ',' identificadores;

usando:         FROM IDENTIFIER WHERE;

condicao:       identificadores '=' identificadores | 
                identificadores '=' identificadores AND condicao | 
                identificadores '=' identificadores OR condicao;

%%

int main(){
    printf("Coloque a sentenca:\n");
    yyparse();
}

