"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2 - Segunda, etc.), se digitar outro valor deve aparecer valor 
inválido.
"""

dia = int(input("Digite o dia da semana:"))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 2:
    print("Terça")
elif dia == 3:
    print("Quarta")
elif dia == 4:
    print("Quinta")
elif dia == 5:
    print("Sexta")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Entrada Invalida")