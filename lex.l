%{
    #include <stdio.h>
    #include "y.tab.h"
    extern int yylval;
%}

// Este e o mapeamento dos comandos que serao analisados
%%
select					return SELECT;
from					return FROM;
where					return WHERE;
and						return AND;
or                      return OR;
[*]						return *yytext;
[,]						return *yytext;
[=]						return *yytext;
[a-zA-Z][a-zA-Z0-9]+	return IDENTIFIER;
\n                      return *yytext;
[ \t]				;
%%
