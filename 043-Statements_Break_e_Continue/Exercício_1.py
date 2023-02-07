"""
São dados dois números inteiros positivos p e q,
sendo que o número de dígitos de p é menor ou igual ao número de dígitos de q.
Verificar se p é um subnúmero de q.

Exemplos:
p = 23, q = 57238, p é subnúmero de q.
p = 23, q = 258347, p não é subnúmero de q.

Reescreva o exercício usando funções, break e continue
"""
def main():
    """
    Função Principal do programa
    """
    p = int(input("Digite o valor de p: "))
    q = int(input("Digite o valor de q: "))

    #Calcula o numero de digitos de p
    cont_d = contaDigitos(p)

    #Comparação
    #p é sub de q --> paro execução
    #q == 0
    aux_q = q
    while True:
        subnum = aux_q%(10**cont_d)
        if subnum == p:
            break

        aux_q //= 10
    
        if aux_q == 0:
            break

    if subnum == p:
        print("%i é subnumero de %i" %(p, q))
    else:
        print("%i não é subnumero de %i" %(p, q))


def contaDigitos(num):
    """
    Recebe um numero inteiro e devolve o número
    de dígitos que esse número possuí
    """
    cont = 0
    while num!=0:
        num //=10
        cont+=1

    return cont

main()




"""
def main():

p=23
q=1239

cont_d = contaDigitos(23)
--------------------------------------------------
def contaDigitos(23):
   
    Recebe um numero inteiro e devolve o número
    de dígitos que esse número possuí

    cont = 0
    while 23!=0:
        num //=10 = 23//10 = 2
        cont+=1

     while 2!=0:
        num //=10 = 2//10 = 0
        cont+=1

	 while 0!=0:(False)****Nao executa
        num //=10 = 2//10 = 0
        cont+=2

    return 2

------------------------------------------------------------------------

cont_d = 2


aux_q = 1239

    while True:
        subnum = aux_q%(10**cont_d) = 1239%(10**2) = 1239%(100) = 39
        if subnum = 39 == p = 23: (False)***Nao executa
            break


	aux_q //= 10 = 1239 //= 10 = 123

    if aux_q  == 0: 123 == 0(False)***Nao executa
            break
------------------------------------------------------------------------

	while True:
         subnum = aux_q%(10**cont_d) = 123%(10**2) = 123%(100) = 23
		subnum = 123%(10**2) = 123%(100)
		subnum = 23        

		if subnum = 23 == p = 23: (True)***Executa
            break ****aqui ele sai do ciclo while na hora


-------------------------------------------------------------------------

    if subnum = 23 == p = 23:(True)***Executa
        print("%i é subnumero de %i" %(23, 1239))
    
	else:
        print("%i não é subnumero de %i" %(p, q))
"""