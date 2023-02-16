"""
Escreva um programa que receba quantas entradas o usuário desejar e depois
crie um novo contato para cada entrada (Nome, Telefone, Endereço, Email), e
por fim imprima, em ordem alfabética, a agenda de contatos 
"""

nomes = [] # Cria uma lista vazia
agenda = {} # Cria um dicionario vazio

while True:
    ordem = input('Deseja adicionar um novo contato(add) ou parar a execução(stop): \n').lower() # Verifica se o usuario quer adicionar mais um contato

    if not ordem.isalpha(): # Verifica se o usuario digitou apenas letras
        print("Digite apenas letras!")
        
    elif ordem.startswith('a'): #Se entrar nessa condicao o usuario vai inserir um novo contato
        contato = {} # Cria um dicionario vazio 


        nome = input('Digite o nome do contato: ') # Recebe o nome digitado pelo usuario 
        if not nome[0].isupper(): # Verifica se a primeira letra do nome eh maiuscula
            nome = nome[0].upper() + nome[1:] # Transforma a primeira letra do nome em maiuscula, caso já não seja

        nomes.append(nome) # Acrescenta o nome digitado(que passa a ser chave de dicionario) a lista de nomes, nomes = ['A', 'B']

        tel = input('Digite o telefone do contato: ') # Recebe o telefone digitado pelo usuario
        contato['Telefone'] = tel # Recebe o valor tel digitado pelo usuario na chave 'Telefone'

        end = input('Digite o endereço do contato: ') # Recebe o endereço digitado pelo usuario
        contato['Endereço'] = end # Recebe o valor end digitado pelo usuario na chave 'Endereço'

        email = input('Digite o Email do contato: ') # Recebe o email digitado pelo usuario 
        contato['Email'] = email # Recebe o o valor email digitado pelo usuario na chave 'Email'

        agenda[nome] = contato # Adiciona o dicionario contato, que ja tem as chaves Telefone, Endereço e Email a lista nome que eh uma chave do dicionario agenda
        print(contato)
        print('\n')
        print(nomes)
        print('\n')  
        print(nome)
        print('\n')
        print(agenda)
        print('\n')

    elif ordem.startswith('s'):
        break

print('A G E N D A\n')
nomes.sort()
for nome in nomes:
    print('Nome: ', nome)
    print('Telefone: ', agenda[nome]['Telefone'])
    print('Endereço: ', agenda[nome]['Endereço'])
    print('Email: ', agenda[nome]['Email'])
    print()