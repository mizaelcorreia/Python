"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os dois vetores.
"""

PAR = []
IMPAR = []
NUMERO = []

for i in range(1, 5):
    num = int(input("Digite o número %i de 20: "%i))
    
    NUMERO.append(num)

    if num%2 == 0:
        PAR.append(num)
    else:
        IMPAR.append(num)

print("Pares: ", PAR)
print("Impares: ", IMPAR)

print("Numeros: ", NUMERO)
print("Pares: ", PAR)
print("Impares: ", IMPAR)