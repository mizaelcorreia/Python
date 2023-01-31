"""
Peça uma lista de números inteiros para o usuário
e imprima a lista sem repetições
"""

n = int(input("Digite o número de elementos da lista: "))

lista = []#Lista original
aux = []#Onde sera feita uma copia da lista

for i in range(n):
    elemento = int(input("Digite o elemento %i de %i: "%(i+1, n)))#Le o elemento seguinte elemento da lista
    lista.append(elemento)#Adiciona o elemento a lista
    aux.append(elemento)#Adiciona o elemento a lista auxiliar

print(lista)#Imprime a lista mesmo havendo elementos repetidos

for ele in aux:#Percorre a lista auxiliar
    aparições = lista.count(ele)#Conta quantas vezes o elemento "ele" aparece na lista
    for i in range(aparições-1):#Percorre a quantidade de vezes repetidas que o elemento aparece na lista
        lista.remove(ele)#Remove o elemento da lista, lembrando sobra 1 elemento, só tirando as vezes que ele aparece repetidamento

print(lista)