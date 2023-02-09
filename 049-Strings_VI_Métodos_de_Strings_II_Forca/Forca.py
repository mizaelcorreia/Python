import random

FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palavras = 'formiga babuino encefalo elefante girafa hamburger chocolate giroscópio'.split()

def main():
    """
    Função Principal do programa
    """
    global FORCAIMG

    print('F O R C A')
    letrasErradas = ''
    letrasAcertadas = ''
    palavraSecreta = geraPalavraAleatória().upper()
    jogando = True

    while jogando:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)

        palpite = recebePalpite(letrasErradas + letrasAcertadas)

        if palpite in palavraSecreta:
            letrasAcertadas += palpite

            if VerificaSeGanhou(palavraSecreta, letrasAcertadas):
                print("Exato! A palavra secreta é "+palavraSecret+'! Você ganhou!!')
                jogando = False
        else:
            letrasErradas += palpite

            if len(letrasErradas) == len(FORCAIMG) - 1:
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)

                print("Você excedeu o seu limite de palpites!")
                print("Depois de "+str(len(letrasErradas))+' letras erradas e'+str(len(letrasAcertadas)), end = ' ')
                print('palpites corretos, a palavra era '+palavraSecreta+'.')

                jogando = False

        if not jogando:
            if JogarNovamente():
                letrasErradas = ''
                letrasAcertadas = ''
                jogando = True
                palavraSecreta = geraPalavraAleatória().upper()

def geraPalavraAleatória():
    """
    Função que retorna uma string a partir da
    lista de palavras global
    """
    global palavras
    return random.choice(palavras)

def imprimeComEspaços(palavra):
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaço entre suas letras ou strings
    """
    for letra in palavra:
        print(letra, end = ' ')

    print()

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    """
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta
    """
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)]+'\n')

    print("Letras Erradas:", end = ' ')
    imprimeComEspaços(letrasErradas)

    vazio = '_'*len(palavraSecreta)
    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]

    imprimeComEspaços(vazio)

def recebePalpite(palpitesFeitos):
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado
    """
    while True:
        palpite = input("Advinhe uma letra.\n").upper()

        if len(palpite) != 1:
            print("Coloque uma única letra.")
        elif palpite in palpitesFeitos:
            print("Você já chutou esta letra. Escolha novamente.")
        elif not 'A' <= palpite <= 'Z':
            print("Por favor escolha apenas letras.")
        else:
            return palpite
        
def JogarNovamente():
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """
    return input("Você quer jogar novamente? (sim ou nao)\n").upper().startswith('S')

def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    """
    Função que verifica se o usuário acertou todas as
    letras da palavra secreta
    """
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break

    return ganhou

main()

"""
F O R C A


  +---+
  |   |
      |
      |
      |
      |
=========

Letras Erradas: 
_ _ _ _ _ _ 
Advinhe uma letra.
w


  +---+
  |   |
  O   |
      |
      |
      |
=========

Letras Erradas: W 
_ _ _ _ _ _ 
main()

global FORCAIMG = é o desenho

print('F O R C A')

letrasErradas = ''

letrasAcertadas = ''

palavraSecreta = geraPalavraAleatória().upper()
Palavra Global:

palavras = 'formiga babuino encefalo elefante girafa hamburger chocolate giroscópio'.split()

palavras = ['formiga', 'babuino', 'encefalo', 'elefante', 'girafa', 'hamburger', 'chocolate', 'giroscópio']
1ª função: def geraPalavraAleatória():  Função que retorna uma string a partir da lista de palavras global  global palavras return random.choice(palavras)

Digamos que foi escolhida aleatoriamente 'formiga'

linha 72: palavraSecreta = geraPalavraAleatória().upper() palavraSecreta = 'FORMIGA'

jogando = True
while True:

2ª função:

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
def imprimeJogo('', '', 'FORMIGA'):

        global FORCAIMG
    global FORCAIMG = desenhos da forca

	    print(FORCAIMG[len(letrasErradas)]+'\n')
    print(FORCAIMG[0]+ pula linha)

''' +---+ | | | | | | ========='''

        print("Letras Erradas:", end = ' ')
    
Tela:	Letras Erradas: W   --> só exemplo

3ª função:

       imprimeComEspaços(letrasErradas)

       def imprimeComEspaços(''):
d
		for letra in palavra:
	for '' in '':

    	    print('', end = ' ')



        vazio = '_'*len(palavraSecreta)
    vazio = '_'*len('FORMIGA')
    vazio = '_'*7


        for i in range(len(palavraSecreta)):
    for i in range(len('FORMIGA'):
    for i=0 até 6:

            if palavraSecreta[i] in letrasAcertadas:
	if palavraSecreta[0] in '':
	if 'F' in ''(False):
		vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]

        imprimeComEspaços(vazio)
    imprimeComEspaços('_'*7)

Chama novamente a 3ª função:

def imprimeComEspaços(palavra):
def imprimeComEspaços('_'*7):

        for letra in palavra:
    for letra in '_'*7:

    print(letra, end = ' ')

Tela _ _ _ _ _ _ _


	     print()

volta para 2ª função finalizando a função imprimeJogo e voltando para main()

palpite = recebePalpite(letrasErradas + letrasAcertadas)
palpite = recebePalpite('' + '')
palpite = recebePalpite('')

chama 4ª função: def recebePalpite(palpitesFeitos): def recebePalpite(''):

while True:
    palpite = input("Advinhe uma letra.\n").upper()
palpite = 'A'

    if len(palpite) != 1:
if 1 != 1(False):
        print("Coloque uma única letra.")

    elif palpite in ''(False):
        print("Você já chutou esta letra. Escolha novamente.")

    elif not 'A' <= palpite <= 'Z':
elif not 'A' <= 'A' <= 'Z'(False): --> se não for verdade é True
        print("Por favor escolha apenas letras.")

    else:
        return palpite
    return 'A'

Voltando para main(), linha 78

palpite = 'A'

	if 'A' in 'FORMIGA':
	     letrasAcertadas = letrasAcertadas + palpite
	     letrasAcertadas = '' + A
	     letrasAcertadas = 'A'

chama 5ª função: if VerificaSeGanhou(palavraSecreta, letrasAcertadas): if VerificaSeGanhou('FORMIGA', 'A'):

			     ganhou = True
			     for letra in palavraSecreta:
		     for 'F' in 'FORMIGA':

   				 if letra not in letrasAcertadas:
			 if 'F' not in 'A'(True):

      		             ganhou = False
        			     break

No break ele já sai direto da função para main()

main() e verifica se a linha 83 é True, como não foi volta pra linha 98:

if not jogando:
if not True:
if False:

voltando pro While: while True:

2ª função:

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
def imprimeJogo('', 'A', 'FORMIGA'):

        global FORCAIMG
    global FORCAIMG = desenhos da forca

	    print(FORCAIMG[len(letrasErradas)]+'\n')
    print(FORCAIMG[0]+ pula linha)

''' +---+ | | | | | | ========='''

        print("Letras Erradas:", end = ' ')
    
Tela:	Letras Erradas:    --> só exemplo
3ª função:

       imprimeComEspaços(letrasErradas)

       def imprimeComEspaços(''):

		for letra in palavra:
	for '' in '':

    	    print('', end = ' ')



        vazio = '_'*len(palavraSecreta)
    vazio = '_'*len('FORMIGA')
    vazio = '_'*7


        for i in range(len(palavraSecreta)):
    for i in range(len('FORMIGA'):
    for i=0 até 6:

            if palavraSecreta[i] in letrasAcertadas:
	if palavraSecreta[0] in 'A':
	if 'A' in 'A'(False):
		vazio = vazio[:6] + palavraSecreta[6] + vazio[7:]
		vazio = '_' + A + ''


        imprimeComEspaços(vazio)
    imprimeComEspaços(_ _ _ _ _ _ A)


"""
    