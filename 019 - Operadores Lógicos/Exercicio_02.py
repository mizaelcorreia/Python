"""
Dados dois números inteiros positivos i e j diferentes de 0,
imprimir todos os divisores comuns de i e j.

Exemplo: i = 2 e j = 3 a saída deverá ser : 1
i = 9, j = 21 a saída deverá ser: 1, 3
"""

i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))

print("Os divisores comuns de %i e %d são: "%(i, j))
print(1)
divisor = 2
while divisor <= i and divisor <= j:
    if i % divisor == 0 and j % divisor == 0:
        print(divisor)
    divisor += 1

print(divisor)


"""
Dados dois números inteiros positivos i e j diferentes de 0,
imprimir todos os divisores comuns de i e j.

Exemplo: i = 2 e j = 3 a saída deverá ser : 1
i = 9, j = 21 a saída deverá ser: 1, 3


i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))

print("Os divisores comuns de %i e %d são: "%(i, j))
print(1)
divisor = 2
while divisor <= i and divisor <= j:
    if i % divisor == 0 and j % divisor == 0:
        print(divisor)
    divisor += 1



i = 9
j = 21

print("Os divisores comuns de %i e %d são: "%(9, 21))
print(1)
divisor = 2
while 2 <= 9 and 2 <= 21:
	if 9 % 2 == 0 and 21 % 2 == 0:False***nao executa
		print(divisor)
	divisor = 2 + 1 = 3



__________________________________________________________



i = 9
j = 21

print("Os divisores comuns de %i e %d são: "%(9, 21))
print(1)
divisor = 2
while 3 <= 9 and 3 <= 21:
	if 9 % 3 == 0 and 21 % 3 == 0:True***executa
		print(3)
	divisor = 3 + 1 = 4



__________________________________________________________



i = 9
j = 21

print("Os divisores comuns de %i e %d são: "%(9, 21))
print(1)
divisor = 2
while 4 <= 9 and 4 <= 21:
	if 9 % 4 == 0 and 21 % 4 == 0:False***nao executa
		print(divisor)
	divisor = 4 + 1 = 5



__________________________________________________________



i = 9
j = 21

print("Os divisores comuns de %i e %d são: "%(9, 21))
print(1)
divisor = 2
while 5 <= 9 and 5 <= 21:
	if 9 % 5 == 0 and 21 % 5 == 0:False***nao executa
		print(divisor)
	divisor = 5 + 1 = 6



__________________________________________________________




i = 9
j = 21

print("Os divisores comuns de %i e %d são: "%(9, 21))
print(1)
divisor = 2
while 6 <= 9 and 6 <= 21:
	if 9 % 6 == 0 and 21 % 6 == 0:False***nao executa
		print(divisor)
	divisor = 6 + 1 = 7



__________________________________________________________






i = 9
j = 21

print("Os divisores comuns de %i e %d são: "%(9, 21))
print(1)
divisor = 2
while 7 <= 9 and 7 <= 21:
	if 9 % 7 == 0 and 21 % 7 == 0:False***nao executa
		print(divisor)
	divisor = 7 + 1 = 8


__________________________________________________________




i = 9
j = 21

print("Os divisores comuns de %i e %d são: "%(9, 21))
print(1)
divisor = 2
while 8 <= 9 and 8 <= 21:
	if 9 % 8 == 0 and 21 % 8 == 0:False***nao executa
		print(divisor)
	divisor = 8 + 1 = 9


__________________________________________________________




i = 9
j = 21

print("Os divisores comuns de %i e %d são: "%(9, 21))
print(1)
divisor = 2
while 9 <= 9 and 9 <= 21:
	if 9 % 9 == 0 and 21 % 9 == 0:False***nao executa
		print(divisor)
	divisor = 9 + 1 = 10


__________________________________________________________




i = 9
j = 21

print("Os divisores comuns de %i e %d são: "%(9, 21))
print(1)
divisor = 2
while 10 <= 9 and 10 <= 21: #False***nao executa
	if 9 % 6 == 0 and 21 % 6 == 0:False***nao executa
		print(divisor)
	divisor = 9 + 1 = 10


__________________________________________________________

"""