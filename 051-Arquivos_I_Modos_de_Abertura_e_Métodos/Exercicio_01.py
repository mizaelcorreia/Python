"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em
disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt", no
seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.
"""

def main():
    arquivo = open("usuarios.txt", 'r')

    linha = arquivo.readline()
    #print(linha)
    espaçoTotal = 0
    usuarios = []
   
    while linha != '':
        separado = linha.split()
        #print(separado)
        removeEspaços(separado)

        espaçoTotal += int(separado[1])
        #print(espaçoTotal)
        #print(espaçoTotal)
        usuarios.append(separado)
        #print(usuarios)
        linha = arquivo.readline()
        #print(linha)
    arquivo.close()

    #print(espaçoTotal)
    espaçoTotal /= (1024**2)
    #print(espaçoTotal)

    geraRelatorio(usuarios, espaçoTotal)

def removeEspaços(splited):
    #print(splited)
    while splited.count('') != 0:
        
        splited.remove('')

def geraRelatorio(usuarios, espaçoTotal):
    relatorio = open('relatorio.txt', 'w')

    CalculaEspaçoUtilizado(usuarios)
    porc = CalculaPorcentagem(usuarios, espaçoTotal)

    relatorio.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    relatorio.write(72*'-' + '\n')
    relatorio.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    maior = EspaçosASeremColocados(usuarios)

    relatorio.write('\n')
    
    for i in range(len(usuarios)):
        
        linha = '%i'%(i+1)
        
        linha += (5-len(linha))*' '
        #print(len(linha))
        
        linha += usuarios[i][0] + (15 - len(usuarios[i][0]))*' '
        print(linha)
        num = "%.2f"%usuarios[i][1]
        espaço_inicio = (maior - len(num))*' '
        num += ' MB'
        espaço_fim = (23 - len(espaço_inicio)-len(num))*' '
        linha += espaço_inicio + num + espaço_fim

        porcentagem = "%.2f"%porc[i]
        espaço_inicio = (5 - len(porcentagem))*' '
        linha += espaço_inicio + porcentagem + "%"

        relatorio.writelines(linha + '\n')

    relatorio.write('\n')
    relatorio.write('Espaço total ocupado: %.2f'%espaçoTotal + '\n')
    relatorio.write('Espaço médio ocupado: %.2f'%(espaçoTotal/len(usuarios)) + '\n')
    relatorio.close()

def CalculaEspaçoUtilizado(usuarios):
    for i in range(len(usuarios)):
        usuarios[i][1] = float(usuarios[i][1])/(1024**2)

def CalculaPorcentagem(usuarios, espaçoTotal):
    porc = []
    for usuario in usuarios:
        porc.append(100*usuario[1]/espaçoTotal)

    return porc

def EspaçosASeremColocados(usuarios):
    maior_string = 0
    for usuario in usuarios:
        if len("%.2f"%usuario[1]) > maior_string:
            maior_string = len("%.2f"%usuario[1])
            #print(maior_string)
    return maior_string
    
main()

"""

def main():
    arquivo = open("usuarios.txt", 'r')

    linha = arquivo.readline()
    linha = "alexandre       456123789"

    espaçoTotal = 0
    usuarios = []

****1ª vez do ciclo

    while linha != ''(True): -------> Esse ciclo preenche as linhas enquanto abrir uma linha com informaçao
        separado = linha.split() ---> cria uma lista com os elementos da da string, separados por um espaço
        separado = ['alexandre', '456123789']
        
        removeEspaços(separado)
        removeEspaços(['alexandre', '456123789'])

-----------------------------------------------------------------------------------------------
Executa removeEspaços (1ª vez)

def removeEspaços(splited):
    while splited.count('') != 0:
        splited.remove('')

def removeEspaços(['alexandre', '456123789']):
    while ['alexandre', '456123789'].count('') != 0:
        splited.remove('')

-----------------------------------------------------------------------------------------------

        espaçoTotal += int(separado[1])
        espaçoTotal += int("456123789") ------> transforma essa parte da string em inteiro 
        espaçoTotal  = 0 + 456123789 = 456123789

        usuarios.append(separado)
        usuarios.append(['alexandre', '456123789'])
        usuarios = ['alexandre', '456123789']  

        linha = arquivo.readline() --------> Le a segunda linha
        linha = "anderson        1245698456"

.
.
.


****2ª vez do ciclo

while linha != ''(True): -------> Esse ciclo preenche as linhas enquanto abrir uma linha com informaçao
        separado = linha.split() 
        separado = ['anderson', '1245698456']
        
        removeEspaços(separado)
        removeEspaços(['anderson', '1245698456'])

-----------------------------------------------------------------------------------------------
Executa removeEspaços (2ª vez)

def removeEspaços(splited):
    while splited.count('') != 0:
        splited.remove('')

def removeEspaços(['anderson', '1245698456']):
    while ['anderson', '1245698456'].count('') != 0:
        splited.remove('')

-----------------------------------------------------------------------------------------------

        espaçoTotal += int(separado[1])
        espaçoTotal += int("1245698456") ------> transforma essa parte da string em inteiro 
        espaçoTotal  = 456123789 + 1245698456= 1.701.822.245

        usuarios.append(separado)
        usuarios.append(['alexandre', '456123789'])
        usuarios = [['alexandre', '456123789'], ['anderson', '1245698456']]  

        linha = arquivo.readline() --------> Le a 3 linha do arquivo
        linha = "antonio         123456456"




*****3ª vez do ciclo

while linha != ''(True): -------> Esse ciclo preenche as linhas enquanto abrir uma linha com informaçao
        separado = linha.split() ---> cria uma lista com os elementos da da string, separados por um espaço
        separado = ['antonio', '123456456']
        
        removeEspaços(separado)
        removeEspaços(['antonio', '123456456'])

-----------------------------------------------------------------------------------------------
Executa removeEspaços (3ª vez)

def removeEspaços(splited):
    while splited.count('') != 0:
        splited.remove('')

def removeEspaços(['antonio', '123456456']):
    while ['antonio', '123456456'].count('') != 0:
        splited.remove('')

-----------------------------------------------------------------------------------------------

        espaçoTotal += int(separado[1])
        espaçoTotal += int("123456456") ------> transforma essa parte da string em inteiro 
        espaçoTotal  = 1.701.822.245 + 123456456 = 1.825.278.701

        usuarios.append(separado)
        usuarios.append(['antonio', '123456456'])
        usuarios = [['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456']]

        linha = arquivo.readline() --------> Le a 4 linha
        linha = "carlos          91257581"


*****4ª vez do ciclo

while linha != ''(True): -------> Esse ciclo preenche as linhas enquanto abrir uma linha com informaçao
        separado = linha.split() ---> cria uma lista com os elementos da da string, separados por um espaço
        separado = ['carlos', '91257581']
        
        removeEspaços(separado)
        removeEspaços(['carlos', '91257581'])

-----------------------------------------------------------------------------------------------
Executa removeEspaços (4ª vez)

def removeEspaços(splited):
    while splited.count('') != 0:
        splited.remove('')

def removeEspaços(['carlos', '91257581']):
    while ['carlos', '91257581'].count('') != 0:
        splited.remove('')

-----------------------------------------------------------------------------------------------

        espaçoTotal += int(separado[1])
        espaçoTotal += int("91257581") ------> transforma essa parte da string em inteiro 
        espaçoTotal  = 1.825.278.701 + 91257581 = 1.916.536.282
        usuarios.append(separado)
        usuarios.append(['carlos', '91257581'])
        usuarios = [['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581']]

        linha = arquivo.readline() --------> Le a 5 linha
        linha = "cesar           987458"
.
.
.
*****5ª vez do ciclo

while linha != ''(True): -------> Esse ciclo preenche as linhas enquanto abrir uma linha com informaçao
        separado = linha.split() ---> cria uma lista com os elementos da da string, separados por um espaço
        separado = ['cesar', '987458']
        
        removeEspaços(separado)
        removeEspaços(['cesar', '987458'])

-----------------------------------------------------------------------------------------------
Executa removeEspaços (5ª vez)

def removeEspaços(splited):
    while splited.count('') != 0:
        splited.remove('')

def removeEspaços(['cesar', '987458']):
    while ['cesar', '987458'].count('') != 0:
        splited.remove('')

-----------------------------------------------------------------------------------------------

        espaçoTotal += int(separado[1])
        espaçoTotal += int("987458") ------> transforma essa parte da string em inteiro 
        espaçoTotal  = 1.916.536.282 + 987458 = 1.917.523.740

        usuarios.append(separado)
        usuarios.append(['cesar', '987458'])
        usuarios = [['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458']]


        linha = arquivo.readline() --------> Le a 6 linha
        linha = "rosemary        789456125"

.
.
.
*****6ª vez do ciclo

while linha != ''(True): -------> Esse ciclo preenche as linhas enquanto abrir uma linha com informaçao
        separado = linha.split() ---> cria uma lista com os elementos da da string, separados por um espaço
        separado = ['rosemary', '789456125']
        
        removeEspaços(separado)
        removeEspaços(['rosemary', '789456125'])

-----------------------------------------------------------------------------------------------
Executa removeEspaços

def removeEspaços(splited):
    while splited.count('') != 0:
        splited.remove('')

def removeEspaços(['rosemary', '789456125']):
    while ['rosemary', '789456125'].count('') != 0:
        splited.remove('')

-----------------------------------------------------------------------------------------------

        espaçoTotal += int(separado[1])
        espaçoTotal += int("789456125") ------> transforma essa parte da string em inteiro 
        espaçoTotal  = 1.917.523.740 + 789456125 = -----

        usuarios.append(separado)
        usuarios.append(['rosemary', '789456125'])
        usuarios = [['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458'], ['rosemary', '789456125']]

        linha = arquivo.readline() --------> Verifica que não há mais nada para ler e retorna string vazia
        linha = ""


*****7ª vez do ciclo

while linha != ''(False): ----->nao executa

    arquivo.close()

    espaçoTotal /= (1024**2) ------>transforma de bytes para MBytes

    geraRelatorio(usuarios, espaçoTotal)
    geraRelatorio(['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458'], ['rosemary', '789456125'], 2.706.979.865)
    

--------------------------------------------------------------------------------------------------------------------------------------------------
Executa função geraRelatorio


def geraRelatorio(['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458'], ['rosemary', '789456125'], 2.706.979.865):
    relatorio = open('relatorio.txt', 'w')


    CalculaEspaçoUtilizado(usuarios)
    CalculaEspaçoUtilizado([['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458'], ['rosemary', '789456125']])


-------------------------------------------------------------------------------------------------------------------------------------------------   
Executa função CalculaEspaçoutilizado

def CalculaEspaçoUtilizado(usuarios):
def CalculaEspaçoUtilizado([['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458'], ['rosemary', '789456125']])
    for i in range(len(usuarios)):
    for 0 in range(6):
	    usuarios[i][1] = float(usuarios[i][1])/(1024**2) ---------> Pega o segundo elemento de cada submatriz e transforma o numero de bytes em Mbytes 
        usuarios[0][1] = 456123789/(1024**2)

    for 1 in range(6):
	    usuarios[i][1] = float(usuarios[i][1])/(1024**2) 
        usuarios[1][1] = 1245698456/(1024**2)
	

    for 2 in range(6):
	    usuarios[i][1] = float(usuarios[i][1])/(1024**2) 
        usuarios[2][1] = 123456456/(1024**2)
	

    for 3 in range(6):
	    usuarios[i][1] = float(usuarios[i][1])/(1024**2)
        usuarios[3][1] = 91257581/(1024**2)
	

    for 4 in range(6):
	    usuarios[i][1] = float(usuarios[i][1])/(1024**2)
        usuarios[4][1] = 987458/(1024**2)
	
    for 5  in range(6):
	    usuarios[i][1] = float(usuarios[i][1])/(1024**2)
        usuarios[5][1] = 789456125/(1024**2)
	

--------------------------------------------------------------------------------------------------------------------------------------------------
continuando a função main	



    porc = CalculaPorcentagem(usuarios, espaçoTotal)
    porc = CalculaPorcentagem([['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458'], ['rosemary', '789456125']], 2.706.979.865)
-------------------------------------------------------------------------------------------------------------------------------------------------
Executa a função CalculaPorcentagem


def CalculaPorcentagem(usuarios, espaçoTotal):
def CalculaPorcentagem([['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458'], ['rosemary', '789456125']], 2.706.979.865):
    porc = []
    for usuario in usuarios:
        porc.append(100*usuario[1]/espaçoTotal)------>Pega o espaço ocupado por cada usuario já transformado em Mbytes e ve a porcentagem que ocupa em relação ao total

    for 0 in 6:
        porc.append(100*456123789/espaçoTotal)

    for usuario in usuarios:
        porc.append(100*1245698456/espaçoTotal)

    for usuario in usuarios:
        porc.append(100*91257581/espaçoTotal)

    for usuario in usuarios:
        porc.append(100*987458/espaçoTotal)

    for usuario in usuarios:
        porc.append(100*789456125/espaçoTotal)


    return porc ---------------->vetor das porcentagens calculadas


---------------------------------------------------------------------------------------------------------------------------------------------------

continuando a função main



    relatorio.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    relatorio.write(72*'-' + '\n')
    relatorio.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    maior = EspaçosASeremColocados(usuarios)




----------------------------------------------------------------------------------------------------------------------------------------------------









    maior = EspaçosASeremColocados([['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458'], ['rosemary', '789456125']], 2.706.979.865)

---------------------------------------------------------------------------------------------------------------------------------------------------

Executa a função EspaçosASeremColocados(usuarios)

def EspaçosASeremColocados(usuarios):
def EspaçosASeremColocados([['alexandre', '456123789'], ['anderson', '1245698456'], ['antonio', '123456456'], ['carlos', '91257581'], ['cesar', '987458'], ['rosemary', '789456125']]):


    maior_string = 0
    for usuario in usuarios: ------>Percorre o vetor de usuarios
        if len("%.2f"%usuario[1]) > maior_string:-------->ve se a quantidade de caracteres do string é maior que a maior string
            maior_string = len("%.2f"%usuario[1])



    return maior_string = 7





--------------------------------------------------------------------------------------------------------------------------------------------------
continuando a função main 


	maior = 7


    relatorio.write('\n')
    
 
    for i in range(len(usuarios)):
        
        linha = '%i'%(i+1) ------> Imprime o numero
        linha += (5-len(linha))*' ' ------> Coloca o espaço na frente do numero

        linha += usuarios[i][0] + (15 - len(usuarios[i][0]))*' ' ------> Coloca nome e pula a quantidade de espaços, se o nome for maior pula menos linhas

        num = "%.2f"%usuarios[i][1]
        espaço_inicio = (maior - len(num))*' '
        num += ' MB'
        espaço_fim = (23 - len(espaço_inicio)-len(num))*' '
        linha += espaço_inicio + num + espaço_fim

        porcentagem = "%.2f"%porc[i]
        espaço_inicio = (5 - len(porcentagem))*' '
        linha += espaço_inicio + porcentagem + "%"

        relatorio.writelines(linha + '\n')



    relatorio.write('\n')
    relatorio.write('Espaço total ocupado: %.2f'%espaçoTotal + '\n')
    relatorio.write('Espaço médio ocupado: %.2f'%(espaçoTotal/len(usuarios)) + '\n')
    relatorio.close()






----------------------------------------------------------------------------------------------------------------------------------




def removeEspaços(splited):
    while splited.count('') != 0:
        splited.remove('')

def geraRelatorio(usuarios, espaçoTotal):
    relatorio = open('relatorio.txt', 'w')

    CalculaEspaçoUtilizado(usuarios)
    porc = CalculaPorcentagem(usuarios, espaçoTotal)

    relatorio.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    relatorio.write(72*'-' + '\n')
    relatorio.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    maior = EspaçosASeremColocados(usuarios)

    relatorio.write('\n')
    
    for i in range(len(usuarios)):
        linha = '%i'%(i+1)
        linha += (5-len(linha))*' '

        linha += usuarios[i][0] + (15 - len(usuarios[i][0]))*' '

        num = "%.2f"%usuarios[i][1]
        espaço_inicio = (maior - len(num))*' '
        num += ' MB'
        espaço_fim = (23 - len(espaço_inicio)-len(num))*' '
        linha += espaço_inicio + num + espaço_fim

        porcentagem = "%.2f"%porc[i]
        espaço_inicio = (5 - len(porcentagem))*' '
        linha += espaço_inicio + porcentagem + "%"

        relatorio.writelines(linha + '\n')

    relatorio.write('\n')
    relatorio.write('Espaço total ocupado: %.2f'%espaçoTotal + '\n')
    relatorio.write('Espaço médio ocupado: %.2f'%(espaçoTotal/len(usuarios)) + '\n')
    relatorio.close()

def CalculaEspaçoUtilizado(usuarios):
    for i in range(len(usuarios)):
        usuarios[i][1] = float(usuarios[i][1])/(1024**2)

def CalculaPorcentagem(usuarios, espaçoTotal):
    porc = []
    for usuario in usuarios:
        porc.append(100*usuario[1]/espaçoTotal)

    return porc

def EspaçosASeremColocados(usuarios):
    maior_string = 0
    for usuario in usuarios:
        if len("%.2f"%usuario[1]) > maior_string:
            maior_string = len("%.2f"%usuario[1])

    return maior_string
    
main()

    



"""