"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
vetor a média de cada aluno, imprima o número de alunos com média maior ou
igual a 7.0.
"""
ALUNOS = 10

medias = []

for i in range(1, ALUNOS+1):
    notas = 0
    for j in range(1, 5):#Soma as 4(j) notas do aluno i
        notas += float(input("Digite a nota %i de 4 do aluno %i de %i: "%(j,i,ALUNOS)))

    notas /= 4#Calcula a nota media do aluno

    medias.append(notas)#Nessa lista é adicionada a media de cada aluno

num = 0

for media in medias:#Na lista de medias de cada aluno contadas quantas sao maiores que 7
    if media >= 7.0:
        num += 1

print("O número de alunos com média maior do que 7.0 é", num)
