
# Utilizando LEX em python

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

![title](https://github.com/alkofabricio/lex-yacc/blob/master/Captura%20de%20Tela%202017-12-22%20a%CC%80s%2001.40.03.png)
+ Tente agora digitar alguma sentença incorreta, como por exemplo:
```
	select * from where name=uepb
	select name from table
```
+ Dessa forma, ele irá retornar a mensagem de erro e o analisador encerrará.

![title](https://github.com/alkofabricio/lex-yacc/blob/master/Captura%20de%20Tela%202017-12-22%20a%CC%80s%2001.40.46.png)

## Observações
+ Para instalar a biblioteca necessária no Windows, instale os pacotes necessários através deste tutorial
https://mail.python.org/pipermail/python-list/2011-March/600251.html
