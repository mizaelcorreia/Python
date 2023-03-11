from tkinter import *

i = Tk() # Atribuição para poder usar os metodos da classe e colocar os elementos gráficos

i.title("Brincando") # Metodo que coloca o titulo na janela

i.geometry("400x300") # Definindo o tamanho padrão da janela

texto = Label(i, text = "Meu texto") # Colocando texto na janela
texto.pack()

ent = Entry(i) # Colocando caixa que pode ser preenchida com texto digitado
ent.pack()

b = Button(i, text = "Clique") # Criação do botão com o texto que aparece no botão
b.pack()


i.mainloop()