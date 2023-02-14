
arquivo = open('OlaArquivo.txt', 'w')

# 'w' --> write --> escrever
# 'r' --> read --> ler
# 'a' --> append --> extender

arquivo.write('Chiclete com Banana')
arquivo.write('\n')
arquivo.write('Manga com Leite\n')

arquivo.writelines(['\nOla ', ' arquivo ', ' essa ', ' eh ', ' nossa ', ' primeira ', ' aula '])

arquivo.close()



arquivo = open('OlaArquivo.txt', 'r')
#y= arquivo.readline()
#print(y)
x = arquivo.readlines()
print(x)

arquivo.close()

#arquivo = open('OlaArquivo.txt', 'a')
#arquivo.write('\nNova linha')
#arquivo.close()