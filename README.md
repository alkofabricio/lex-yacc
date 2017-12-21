# lex-yacc
Este é um compilador Lex-Yacc feito em C

+Para executar o compilador você deve estar em uma máquina UNIX, pode ser Mac ou Linux.-
+No Linux, para instalar os pacotes necessários, deve executar os seguintes comandos no terminal:-
```
	sudo apt-get install flex
	sudo apt-get install byaac
```
+Após a instalação dos pacotes, você deve ir pelo terminal até a pasta onde está os arquivos lex.l e yacc.y.-
+Lá deve ser executado os seguintes comandos:-
```
	lex lex.l
	yacc -d yacc.y
```
+Serão criados os arquivos:
++lex.yy.c
++y.tab.c
++y.tab.h
