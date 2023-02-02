"""
Escreva uma função que obtenha o maior número de uma sequência de números
"""

def Max(*nums):
    maior = nums[0]

    for num in nums:
        if num > maior:
            maior = num

    return maior

print(Max(1,2,3,4,5,50000))