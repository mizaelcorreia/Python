def funcao_auxiliar(candidatas_totais):
	arquivo = open("FRASE.txt", "w")
	frase = []
	for i in range(len(candidatas_totais)):
		frase.append("")
	for a0 in range(len(candidatas_totais[0])):
		frase[0]= candidatas_totais[0][a0]
		frase_s = ""
		for palavra in frase:
			frase_s += palavra
			frase_s += " "
		arquivo.write(frase_s + "\n")
	arquivo.close()