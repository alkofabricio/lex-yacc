
# Utilizando LEX e YACC em python

Este é um analisador sintático utilizando <b>python2.7</p>.

## Configuração inicial
+ No <b>Mac</b> ou <b>Linux</b>, para instalar os pacotes necessários, deve executar o seguinte comando no terminal:
```
	pip install ply
```
+ No <b>Windows</b>, siga as instruções do tutorial no final destas anotações.
+ Faça download do arquivo <b>LexSQL.py</b>;
+ Abra o arquivo python no seu IDE preferível e execute. <b>Obs.: Certifique-se de que está usando o python 2.7</b>

## Testando o analisador léxico:
+ Ele ficará aguardando sua sentença.
+ Tente, por exemplo digitar estas linhas de comando:
```
	select * from table1 where name=uepb
	select name from table2 where name=uepb and surname=compiladores
	select name from table2 where name=uepb or outro=compiladores
```
+ Dessa forma, se tudo ocorrer bem, ele irá retornar:
```
	Sintaxe Correta
```

![title](https://github.com/alkofabricio/lex-yacc/blob/master/sucesso.png)
+ Tente agora digitar alguma sentença incorreta, como por exemplo:
```
	select * from where name=uepb
	select name from table
```
+ Dessa forma, ele irá retornar a mensagem de erro e o analisador encerrará;

![title](https://github.com/alkofabricio/lex-yacc/blob/master/falha.png)

+ Para encerrar o analisador, digite o comando <b>quit()</b>.

## Observações
+ Para instalar os pacores necessários no Windows, acesse este tutorial:
https://mail.python.org/pipermail/python-list/2011-March/600251.html
