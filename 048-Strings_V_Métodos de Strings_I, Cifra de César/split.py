"""
Arquivo para .split() e .rsplit()

Escreva uma função que tem como separador padrão caracter
' ' e recebe uma string e devolve um lista contendo a string separada
de acordo com a ocorrência do separador

Exemplo
frase = "Ola meu nome é pedro"
split(frase)
['Ola', 'meu', 'nome', 'é', 'pedro']
"""
def split(frase, separador = ' '):
    lista = []
    palavra = ''
    i = 0

    while i < len(frase):
        if frase[i:i+len(separador)] != separador:
            palavra += frase[i]
          
        else:
            if palavra != '':
                lista.append(palavra)
            i += len(separador)
            palavra = ''
            continue

        i+= 1
  
    print(palavra)
    print(frase[i:])
    print(palavra)
    

    if palavra != '':
        lista.append(palavra)

    return lista

print(split('Ola meu nome é pedro', ' '))


"""

split(frase, separador=' ': split("Ola meu nome é pedro", separador=' ': lista=[] palavra= '' i = 0
while i < len(frase) + 1 - len(separador): while 0 < 20 + 1 - 1: while i=0 < 20(True):

	if frase[i:i+len(separador)] != separador:
	if frase[0:1] != ' '(True):
        		palavra += frase[i]
		palavra = '' + frase[0]= 'O'

while i=1 < 20(True):

	if frase[i:i+len(separador)] != separador:
	if frase[1:2] != ' '(True):
        		palavra += frase[1]
		palavra = 'O' + frase[1]
		palavra = 'O' + 'l' = 'Ol'
while i=2 < 20(True):

	if frase[i:i+len(separador)] != separador:
	if frase[2:3] != ' '(True):
        		palavra += frase[2]
		palavra = 'O' + frase[2]
		palavra = 'Ol' + 'a' = 'Ola'

while i=3 < 20(True):

	if frase[i:i+len(separador)] != separador:
	if frase[3:4] != ' ':
	if frase[3:4] != ' '(False):
        		

    	else:
        		if palavra != '':
		if 'Ola' != '':
           			 lista.append(palavra)
			 lista.append('Ola')

lista=['Ola']
		i = i + len(separador)
		i = 3 + 1 
		i = 4

        		palavra = ''
        		continue  --> vai pro while, não conta

while i=4 < 20(True):

	if frase[i:i+len(separador)] != separador:
	if frase[4:5] != ' ':
	if frase[4:5] != ' '(True):
		palavra += frase[4]
		palavra = '' + frase[4]
		palavra = '' + 'm' = 'm'
        		.
		.
		.
		.
		.
while i=19 < 20(True):

	if frase[i:i+len(separador)] != separador:
	if frase[19:20] != ' ':
	if frase[19:20] != ' '(True):
		palavra += frase[19]
		palavra = 'pedr' + frase[19]
		palavra = 'pedr' + 'o' = 'pedro'
lista = ['Ola', 'meu', 'nome', 'é', 'pedro'] palavra = 'pedro'

while i < len(frase) + 1 - len(separador):
    while i=20 < 20 
palavra = palavra + frase[20:]
palavra = pedro + ''
palavra = 'pedro'

if 'pedro' != '':
	lista = ['pedro']

retunr lista


"""