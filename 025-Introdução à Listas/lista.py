lista=[1,2,3,4,5]

print(lista)
print(lista[2])


for i in range(5):
    print(lista[i])

lista += [7]#Adicionara o elemento apos a ultima posicao

print(lista)

lista += [0,0,0]#Tem como adicionar mais um elemento de uma unica vez
print(lista)

a = lista[2] + lista[3]

print(a)

lista[2] = 7.3

print(lista)

a = 1
b = 2
c = 3
d = 4

lista = [a, b, c, d]

print(lista)

print(lista[-1:-3])