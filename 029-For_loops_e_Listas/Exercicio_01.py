"""
Escreva um programa que crie uma lista de elementos, até se entrar -1,
e depois imprima todos os números da lista que são maiores que 10.
"""

lista = []#Criada uma lista vazia

i = int(input("Digite um número da lista: "))
while i != -1:
    lista.append(i)#Acrescenta o elemento i para lista
    i = int(input("Digite um número da lista: "))#O proximo elemento i para lista

print("Os seguintes números da lista são maiores do que 10")
for num in lista:#Percorre os elementos da lista
    if num > 10:#Verifica se o numero é maior que 10
        print(num)#Imprime o numero maior que 10
