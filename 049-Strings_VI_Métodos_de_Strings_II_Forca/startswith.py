"""
Arquivo para startswith

Escreva uma função que verififica se uma determinada string começa
com uma determinada substring
"""

def startswith(string, sub):
    return string[:len(sub)] == sub

print(startswith('Sim', 'S'))
print(startswith('Sim', 's'))
print(startswith('Sim', 'Si'))

"""

False
False
False
1ª função: def startswith(string, sub): startswith('Sim', 'S'):

        return string[:len(sub)] == sub
    return string[:1] == 'S'
    return 'S' == 'S'
    return True

print(startswith('Sim', 'S'))

    startswith('Sim', 'S'):

        return string[:len(sub)] == sub
    return string[:1] == 's'
    return 'S' == 's'
    return False

print(startswith('Sim', 's'))

    startswith('Sim', 'Si'):

        return string[:len(sub)] == sub
    return string[:1] == 'Si'
    return 'S' == 'Si'
    return False

print(startswith('Sim', 'Si'))

"""