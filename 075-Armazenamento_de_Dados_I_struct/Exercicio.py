"""
Crie um programa para o governo, onde é possível armazenar o nome
de uma Pessoa, R.G. e CPF e depois possa armazenar esses
dados num formato de bytes
"""

import struct #Importando o modulo struct

def main(): # Declarando a função main
    pessoas = carregaListaDeCadastros() # Chamando a função e atribuindo o retorno a uma variavel
    print(pessoas)
    while True:
        cmd = recebeComando()

        if cmd.startswith('n'):
            adicionaCadastro(pessoas)
        elif cmd.startswith('p'):
            if len(pessoas) == 0:
                print('Não há nenhum cadastro')
            else:
                pegaCadastro(pessoas)
        else:
            break

    salvaPessoas(pessoas)
    

def carregaListaDeCadastros(): # Definicão da função que não recebe nenhum argumento
    try: #Tenta abrir o arquivo pessoas utilizando o modulo decode que passa do formato de bytes para o formato literal e usando o modo de leitura binaria
        arq = open('pessoas.decode', 'rb')
    except IOError: #Se o arquivo que tentou ser aberto não existe esse bloco é executado
        return {} # Retorna chaves vazias
    
    else: #Executa caso nenhuma exceção seja tratada
        pessoas = {} # Cria um dicionario vazio chamado pessoas
        
        try:
            #Primeiro dado --> numero de chars do nome
            for num_char_nome in arq: # Percorre cada linha do arquivo 
                num_char_nome = num_char_nome.split(b'\n')[0] # Que informação é essa?


                #Segundo dado --> nome
                #Terceiro dado --> R.G.
                #Quarto dado --> C.P.F
                decode = '%is Q Q'%struct.unpack('I', num_char_nome)[0] # Tipo e nome da variavel 
                
                data = arq.readline().split(b'\n')[0]
                info = struct.unpack(decode, data)

                pessoas[info[0].decode()] = {'R.G.' : info[1], 'C.P.F.': info[2]}

        except:
            print('Há um erro de formatação no arquivo')
            return {}

        else:
            return pessoas

def recebeComando():
    while True:
        cmd = input('Deseja adicionar um novo cadastro(n/novo) ou procurar as informações de um cadastro(p/procurar) ou sair(s/sair)?\n').lower()

        if not cmd.isalpha():
            print('Digite apenas letras!')
        elif cmd.startswith('n') or cmd.startswith('p') or cmd.startswith('s'):
            return cmd
        else:
            print('Não entendi seu comando!')

def adicionaCadastro(pessoas):
    nome = input('Digite o nome do individuo\n')
    pessoas[nome] = {} # Cria chave de dicionario

    pegaRG(pessoas[nome]) # Função que tem com argumento chave de dicionario

    pegaCPF(pessoas[nome]) # Função que tem com argumento chave de dicionario

def pegaRG(pessoas):
    while True:
        RG = input('Digite o RG do individuo\n')
        try:
            separado = RG.split('.') # Quebra a string digitada em subStrings entre os pontos
            primeiros_dois = separado[0]
            segundo_tres = separado[1]
            terceiro_tres = separado[2].split('-')[0]
            ultimo = separado[2].split('-')[1]

            if not (primeiros_dois.isdigit() and segundo_tres.isdigit() and terceiro_tres.isdigit() and ultimo.isdigit()): # Verifica se tudo que foi digitado é numero(digito)
                print('Digite apenas numeros')

            elif len(primeiros_dois) != 2 or len(segundo_tres) != 3 or len(terceiro_tres) != 3 or len(ultimo) != 1: # Verifica se as subString de digitos tem os tamanhos corretos
                print('Numero de algarismos está errado, digite novamente')

        except IndexError:
            print('Entrada inválida')

        except Exception as E:
            print(E)

        else:
            pessoas['R.G.'] = int(primeiros_dois+segundo_tres+terceiro_tres+ultimo)
            break

def pegaCPF(pessoas):
    while True:
        CPF = input('Digite o CPF do individuo\n')
        try:
            separado = CPF.split('.')
            primeiros_tres = separado[0]
            segundo_tres = separado[1]
            terceiro_tres = separado[2].split('/')[0]
            ultimos_dois = separado[2].split('/')[1]

            if not (primeiros_tres.isdigit() and segundo_tres.isdigit() and terceiro_tres.isdigit() and ultimos_dois.isdigit()):
                print('Digite apenas numeros')

            elif len(primeiros_tres) != 3 or len(segundo_tres) != 3 or len(terceiro_tres) != 3 or len(ultimos_dois) != 2:
                print('Numero de algarismos está errado, digite novamente')

        except IndexError:
            print('Entrada inválida')

        except Exception as E:
            print(E)

        else:
            pessoas['C.P.F.'] = int(primeiros_tres+segundo_tres+terceiro_tres+ultimos_dois)
            break


def pegaCadastro(pessoas):
    while True:
        nome = input('Digite o nome da pessoa\n')

        if nome in pessoas:
            formataCadastro(pessoas, nome)
            break
        else:
            print('Pessoas nao encontrada, digite novamente')

def formataCadastro(pessoas, nome):
    print('Nome: %s'%nome)
    imprimeRG(pessoas[nome]['R.G.'])
    imprimeCPF(pessoas[nome]['C.P.F.'])
    print()

def colacaZero(num, palavra):
    if len(palavra) < num:
        return (num - len(palavra))*'0' + palavra
    else:
        return palavra

def imprimeRG(RG):
    ultimo = str(RG%10)
    RG //= 10
    terceiro_tres = colacaZero(3, str(RG%1000))
    RG//=1000
    segundo_tres = colacaZero(3, str(RG%1000))
    RG//=1000
    primeiros_dois = colacaZero(2, str(RG%100))

    print('R.G.: '+primeiros_dois+'.'+segundo_tres+'.'+terceiro_tres+'-'+ultimo)

def imprimeCPF(CPF):
    ultimos_dois = colacaZero(2, str(CPF%100))
    CPF //= 100
    terceiro_tres = colacaZero(3, str(CPF%1000))
    CPF//=1000
    segundo_tres = colacaZero(3, str(CPF%1000))
    CPF//=1000
    primeiros_tres = colacaZero(3, str(CPF%1000))

    print('C.P.F: '+primeiros_tres+'.'+segundo_tres+'.'+terceiro_tres+'/'+ultimos_dois)
    

def salvaPessoas(pessoas):
    with open('pessoas.decode', 'wb') as arq:
        for nome in pessoas:
            num_de_chars = len(nome)
            num_data = struct.pack('I', num_de_chars)
            arq.write(num_data)
            arq.write(b'\n')

            info_data = struct.pack('%is Q Q'%num_de_chars, nome.encode(), pessoas[nome]['R.G.'], pessoas[nome]['C.P.F.'])

            arq.write(info_data)
            arq.write(b'\n')


if __name__ == '__main__':
    main()
