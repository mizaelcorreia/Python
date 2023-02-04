"""
Escreva uma função recursiva que imprima de um número x até um y
"""

def funcaoRecursiva(x, y):

    if x <= y:
        print(x)
        funcaoRecursiva(x+1, y)
    print(x)

funcaoRecursiva(0, 10)