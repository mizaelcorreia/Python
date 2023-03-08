try: 
    a = open('arquivo.txt', 'r') # Abre o arquivo no modo de leitura, caso o arquivo existe, se não nao tem oque ler né
    linha = a.readline() # Atribui a variável linha oque é lido em uma linha da variavel a que contem o arquivo aberto no modo leitura
    linha.split('!') # Quebra a linha quando encontra a string '!'
    linha = linha[0] #Atribui a linha o primeiro elemento da linha
    a.close() # Fecha o arquivo 
    a = open('arquivo.txt', 'a') # Abre denovo o arquivo no modo append
    a.write(linha) # Adiciona ao arquivo o conteudo da variavel linha
except FileNotFoundError: # Quando o erro for desse tipo o programa não interrompe mas executa oque está no bloco, mas se o erro for de outro tipo o programa pode sim ser interrompido
    print('Deu erro!')
    a = open('arquivo.txt', 'w') #Abre o arquivo no modo escrita 
    a.write('ERRO!!!!!') # Escreve essa mensagem no arquivo que foi aberto
finally:
    a.close() # Tendo ou não erro, no final o programa é fechado