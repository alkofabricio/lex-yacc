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

%%
%token SELECT FROM IDENTIFIER WHERE OR AND;

line: selecionar itens usando condicao '\n'{
    printf("Sintaxe Correcta\n");
};

selecionar: SELECT;
itens: '*' | identificadores;
identificadores: IDENTIFIER | IDENTIFIER ',' identificadores;
usando: FROM IDENTIFIER WHERE;
condicao: IDENTIFIER '=' IDENTIFIER | IDENTIFIER '=' IDENTIFIER AND condicao | IDENTIFIER '=' IDENTIFIER OR condicao;

%%

int main(){
    printf("Coloque a sentenca:\n");
    yyparse();
}

