try: #Tenta executar oque tem dentro do bloco
    x = int(input('Digite um numero: '))
except: #Se não for possivel executar o try imprime oque esta nesse bloco e atribui a x o valor de 0
    print('Deu erro!')
    x = 0
finally: #Executando o try ou o except no final ele imprime o x que pode ser o atribuido pelo try ou pelo except
    print(x)