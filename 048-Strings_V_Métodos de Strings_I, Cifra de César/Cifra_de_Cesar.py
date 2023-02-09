TAM_MAX_CH = 26

def recebeModo():
    """
    Função que pergunta se o usuário quer criptografar ou
    decriptografar e garante que uma entrada válida foi recebida
    """

    while True:
        modo = input("Você deseja criptografar ou decriptografar?\n").lower()
        if modo in 'criptografar c decriptografar d'.split():
            return modo
        else:
            print("Entre 'criptografar' ou 'c' ou 'decriptografar' ou 'd'.")

def recebeChave():
    """
    Função que pede o valor da chave para o usuário
    e devolve a chave caso o valor desta esteja adequado
    """
    global TAM_MAX_CH
    chave = 0

    while True:
        chave = int(input('Entre o número da chave (1-%d)\n'%(TAM_MAX_CH)))

        if 1 <= chave <= TAM_MAX_CH:
            return chave

def geraMsgTraduzida(modo, mensagem, chave):
    """
    Traduz a mensagem do usuário de modo conveniente
    """
    if modo[0] == 'd':
        chave *= -1

    traduzido = ''

    for simbolo in mensagem:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            traduzido += chr(num)
        else:
            traduzido += simbolo
    return traduzido

def main():
    """
    Função principal do programa
    """
    modo = recebeModo() 
    mensagem = input("Entre com sua mensagem\n")
    chave = recebeChave()

    print("Seu texto traduzido é:")
    print(geraMsgTraduzida(modo, mensagem, chave))

main()
        
"""

Você deseja criptografar ou decriptografar?
c
Entre sua mensagem
fElipe3
Entre o número da chave (1-26)
2
Seu texto traduzido é:
h
hG
hGn
hGnk
hGnkr
hGnkrg
hGnkrg3
ABCDEFGHIJKLMNOPQRSTUVWXYZ YZABCDEFGHIJKLMNOPQRSTUVWX

fElipe3 ---> decriptografado hGnkrg3 ---> criptografado

for i=65 até 90: c = c + chr(i) c = '' + chr(65) c = '' + A c = 'A'

for i=66 até 90: c = c + chr(i) c = 'A' + chr(66) c = 'A' + B c = 'AB'

.
.
.
.
for i=90 até 90: c = c + chr(i) c = 'ABCDEFGHIJKLMNOPQRSTUVWXY' + chr(90) c = 'ABCDEFGHIJKLMNOPQRSTUVWXY' + Z c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Vai aparecer na tela --> ABCDEFGHIJKLMNOPQRSTUVWXYZ

main() 1ª função:

def recebeModo():

while True:
    modo = input("Você deseja criptografar ou decriptografar?\n").lower()  --> lower() - transforma letras maiusculas em minusculas
modo = criptografar

    if modo in 'criptografar c decriptografar d'.split():   --> a cada espaço quebra strings em strings menores
if criptografar in 'criptografar c decriptografar d'.split():

        return modo= criptografar
    else:
        print("Entre 'criptografar' ou 'c' ou 'decriptografar' ou 'd'.")

main()

modo = criptografar
mensagem = felipe
chave = recebeChave()
2ª função:

def recebeChave():

global TAM_MAX_CH        ---> já determinado no inicio do programa
chave = 0

while True:
    chave = int(input('Entre o número da chave (1-%s)\n'%(TAM_MAX_CH)))

    if 1 <= chave <= TAM_MAX_CH:
if 1 <= 2 <= 26:
        return chave = 2
main()

modo = criptografar
mensagem = fElipe3
chave = 2

print("Seu texto traduzido é:")
	print(geraMsgTraduzida(modo, mensagem, chave))
3ª função:

def geraMsgTraduzida(modo, mensagem, chave): def geraMsgTraduzida(criptografar, fElipe3, 2):

if modo[0] == 'd':
if 'c' == 'd'(False):
    chave *= -1

traduzido = ''

for simbolo in mensagem:
for 'f' in fElipe3:

    if simbolo.isalpha():    --> verificar se é uma letra

        num = ord(simbolo)   --> recebe um número que representa a letra 'f' no formato ASCII
    num = ord('f')
    num = 102

        num = num + chave
    num = 102 + 2
    num = 104           --> o que era 'f' agora vai ser alguma letra que representa posição 104, criptografia

        if simbolo.isupper():
    if 'f'.isupper()(False):       ---> é maiusculo? Não executa
	if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26

        elif simbolo.islower()(True):        ---> é minuscula? Executa
    elif 'f'.islower()(True): 

            if num > ord('z'):    ---> descobri a posição 'z' usando print(ord('z'))
	if 104 > 122(False):
                num -= 26

            elif num < ord('a'):
	elif 104 < 97(False):
                num += 26

        traduzido = traduzido + chr(num)  --> função chr faz uma comparação entre o número e valor do número na ASCII, print(chr(104))
    traduzido = '' + chr(104)
    traduzido = '' + h
    traduzido = 'h'
for 'E' in fElipe3:

    if simbolo.isalpha():    --> verificar se é uma letra

        num = ord(simbolo)   --> recebe um número que representa a letra 'f' no formato ASCII
    num = ord('E')
    num = 69

        num = num + chave
    num = 69 + 2
    num = 71          --> o que era 'f' agora vai ser alguma letra que representa posição 104, criptografia

        if simbolo.isupper():
    if 'E'.isupper()(True):       ---> é maiusculo? Não executa
	if 69 > 90 (False):
                num -= 26
            elif 69 < 65 (False):
                num += 26

        elif simbolo.islower()(False):        ---> é minuscula? Executa
    elif 'E'.islower()(False): 

            if num > ord('Z'):    ---> descobri a posição 'z' usando print(ord('z'))
	if 69 > 90 (False):
                num -= 26

            elif num < ord('A'):
	elif 69 < 65 (False):
                num += 26

        traduzido = traduzido + chr(num)  --> função chr faz uma comparação entre o número e valor do número na ASCII, print(chr(104))
    traduzido = 'h' + chr(71)
    traduzido = 'h' + G
    traduzido = 'hG'
else: traduzido += simbolo . . . . for '3' in felipe:

    if simbolo.isalpha() (False):    --> verificar se é uma letra

        num = ord(simbolo)   --> recebe um número que representa a letra 'f' no formato ASCII
    num = ord('E')
    num = 69

        num = num + chave
    num = 69 + 2
    num = 71          --> o que era 'f' agora vai ser alguma letra que representa posição 104, criptografia

        if simbolo.isupper():
    if 'E'.isupper()(True):       ---> é maiusculo? Não executa
	if 69 > 90 (False):
                num -= 26
            elif 69 < 65 (False):
                num += 26

        elif simbolo.islower()(False):        ---> é minuscula? Executa
    elif 'E'.islower()(False): 

            if num > ord('Z'):    ---> descobri a posição 'z' usando print(ord('z'))
	if 69 > 90 (False):
                num -= 26

            elif num < ord('A'):
	elif 69 < 65 (False):
                num += 26

        traduzido = traduzido + chr(num)  --> função chr faz uma comparação entre o número e valor do número na ASCII, print(chr(104))
    traduzido = 'hGnkr' + chr()
    traduzido = 'hGnkr' + g
    traduzido = 'hGnkrg'     

else:
       		 traduzido = traduzido + simbolo
		 traduzido = 'hGnkrg' + 3
		 traduzindo = 'hGnkrg3'
'

return traduzido

"""