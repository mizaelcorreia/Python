"""
Valores booleanos sao dois objetos constantes Falso e Verdadeiro. Eles são usados
para representar valores verdadeiros (apesar de que outros valores podem ser considerados
falso ou verdadeiro). No contexto numerico (por exemplo quando são usadas como argumento
para uma operação aritimetica), eles se comportam como os inteiros 0 e 1, respectivamente.
A função de construção bool() pode ser usada para converter qualquer valor para um Boolean,
se o valor puder ser interpretado como um valor verdadeiro.

São escritos como False e True, respectivamente

"""

idade = int(input("Digite sua idade: "))
pode = idade >= 18
print(pode)