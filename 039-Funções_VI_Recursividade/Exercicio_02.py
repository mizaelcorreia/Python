"""
Escreva uma função recursiva que retorna a soma de n até zero
"""


def funcaoRecursiva(n):

    if n == 0:
        return n
    return funcaoRecursiva(n-1) + n


print(funcaoRecursiva(10))
print(funcaoRecursiva(3))