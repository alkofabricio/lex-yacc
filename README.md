
# Utilizando LEX e YACC para reconhecer comandos SQL

Este é um compilador Lex-Yacc feito em C

## Configuração inicial
+ Para executar o compilador você deve estar em uma máquina UNIX, pode ser Mac ou Linux.-
+ No Linux, para instalar os pacotes necessários, deve executar os seguintes comandos no terminal:-
```
	sudo apt-get install flex
	sudo apt-get install byaac
```
+ Após a instalação dos pacotes, você deve ir pelo terminal até a pasta onde está os arquivos lex.l e yacc.y.-
+ Lá deve ser executado os seguintes comandos:-
```
	lex lex.l
	yacc -d yacc.y
```
+ Serão criados os arquivos:
```
	lex.yy.c
	y.tab.c
	y.tab.h
```

+ Depois, deve ser executado o seguinte comando no terminal:
```
	gcc lex.yy.c y.tab.c -o ly
```
+ Veja que foi criado um arquivo "ly". No terminal execute o comando:
```
	./ly
```

## Testando o analisador léxico:
+ Ele ficará aguardando sua sentença.
+ Tente, por exemplo digitar estas linhas de comando:
```
	select * from table1 where name=uepb
	select name from table2 where name=uepb and surname=compilad
```
+ Dessa forma, se tudo ocorrer bem, ele irá retornar:
```
	Sintaxe Correta
```
+ Tente agora digitar uma sentença incorreta, como por exemplo:
```
	select * from where name=uepb
	select name from table
```
+ Dessa forma, ele irá retornar a mensagem de erro e o analisador encerrará.

## Observações
+ Para executar o Lex-Yacc no Windows, instale os pacotes necessários através deste tutorial https://www.youtube.com/watch?v=0MUULWzswQE&t=11s
+ O comando surname suporta apenas 8 caracteres.
