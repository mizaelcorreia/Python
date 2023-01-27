"""
Dados n e dois números inteiros positivos i e j diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou
de j e ou de ambos.

Exemplo: Para n = 6 , i = 2 e j = 3 a saída deverá ser : 0,2,3,4,6,8.
"""

n = int(input("Digite n: "))
i = int(input("Digite i: "))
j = int(input("Digite j: "))
nat, cont = 0, 0
while cont < n:
    if nat % i == 0 or nat % j == 0:
        print (nat)
        cont =cont+ 1
    nat = nat + 1


"""
n = 6
i = 2
j = 3

nat, cont = 0, 0

while 0 < 6:
    if 0 % 2 == 0 or 0 % 3 == 0:
        print (0)
        cont = 0 + 1 = 1
    nat = 0 + 1 = 1


________________________________________________________________

while 1 < 6:
    if 1 % 2 == 0 or 1 % 3 == 0:#False***nao executa
        print (nat)
        cont =cont+ 1
    nat = 1 + 1 = 2

_________________________________________________________________


while 1 < 6:
    if 2 % 2 == 0 or 2 % 3 == 0:#True***executa
        print (2)
        cont = 1 + 1 = 2
    nat = 2 + 1 = 3


___________________________________________________________________

while 2 < 6:
    if 3 % 2 == 0 or 3 % 3 == 0:
        print (3)
        cont = 2 + 1 = 3
    nat = 3 + 1 = 4

____________________________________________________________________


while 3 < 6:
    if 4 % 2 == 0 or 4 % 3 == 0:
        print (4)
        cont = 3 + 1 = 4
    nat = 4 + 1 = 5


_____________________________________________________________________

while 4 < 6:
	if 5 % 2 == 0 or 5 % 3 == 0:#False***nao executa
		print (nat)
        	cont =cont+ 1
	nat = 5 + 1 = 6


_____________________________________________________________________

while 4 < 6:
	if 6 % 2 == 0 or 6 % 3 == 0:#True***executa
		print (6)
        	cont = 4 + 1 = 5
	nat = 6 + 1 = 7

_____________________________________________________________________

while 5 < 6:
	if 7 % 2 == 0 or 7 % 3 == 0:#False***nao executa
		print (nat)
        	cont =cont+ 1
	nat = 7 + 1 = 8

_____________________________________________________________________

while 5 < 6:
	if 8 % 2 == 0 or 8 % 3 == 0:#True***executa
		print (8)
        	cont = 5 + 1 = 6
	nat = 8 + 1 = 9

_______________________________________________________________________


while 6 < 6: #False***nao executa
    if nat % i == 0 or nat % j == 0:
        print (nat)
        cont =cont+ 1
    nat = nat + 1

"""