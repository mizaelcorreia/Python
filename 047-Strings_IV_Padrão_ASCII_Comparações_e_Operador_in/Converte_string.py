"""
Faça dois funções: Uma que coloque uma string em maiusculo e outra
que coloque uma str em minusculo
"""
def main():
    string = 'CHiCleTe'

    print(tudoMinusculo(string))
    print(tudoMaiusculo(string))

def tudoMinusculo(string):
    minusculo = ""

    for char in string:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + (ord('a') - ord('A')))
        minusculo += char

    return minusculo

def tudoMaiusculo(string):
    miausculo = ""

    for char in string:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - (ord('a') - ord('A')))
        miausculo += char

    return miausculo

main()

"""
def main():
    string = 'CHiCleTe'

    print(tudoMinusculo(string))
    print(tudoMinusculo(CHiCleTe))

def tudoMinusculo(CHiCleTe):
    minusculo = ""

    for char in string:
        if 'A' <= char <= 'Z':
            char = chr(ord('C') + (ord('a') - ord('A')))
        minusculo += "char"

	for C in CHiCleTe:
        if 'A' <= C <= 'Z':(True)
            char = chr(ord('C') + (ord('a') - ord('A'))) = chr(67 + (97-65)) = chr(99) = c
        minusculo += "c"
	
	for H in CHiCleTe:
        if 'A' <= H <= 'Z':(True)
            char = chr(ord('H') + (ord('a') - ord('A'))) = chr(72 + (97-65)) = chr(104) = h
        minusculo += "ch"
	
	for i in CHiCleTe:
        if 'A' <= i <= 'Z':(False)
            char = chr(ord('i') + (ord('a') - ord('A')))
        minusculo += "chi"
	
	for C in CHiCleTe:
        if 'A' <= C <= 'Z':(True)
            char = chr(ord(char) + (ord('a') - ord('A'))) = chr(67 + (97-65)) = chr(99) = c
        minusculo += chic 
	
	for l in CHiCleTe:
        if 'A' <= l <= 'Z':(False)
            char = chr(ord(char) + (ord('a') - ord('A')))
        minusculo += chicl

	for e in CHiCleTe:
        if 'A' <= e <= 'Z':(False)
            char = chr(ord(char) + (ord('a') - ord('A')))
        minusculo += chicle

	for T in CHiCleTe:
        if 'A' <= T <= 'Z':(True)
            char = chr(ord(char) + (ord('a') - ord('A'))) = chr(84 + (97-65)) = chr(116) = t
        minusculo += chiclete

	for T in CHiCleTe:
		if 'A' <= e <= 'Z':(True)
            char = chr(ord(char) + (ord('a') - ord('A'))) = chr(84 + (97-65)) = chr(116) = t
        minusculo += chiclet


	








    return minusculo





    print(tudoMaiusculo(string))

def tudoMinusculo(string):
    minusculo = ""

    for char in string:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + (ord('a') - ord('A')))
        minusculo += char

    return minusculo

def tudoMaiusculo(string):
    miausculo = ""

    for char in string:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - (ord('a') - ord('A')))
        miausculo += char

    return miausculo

main()



"""