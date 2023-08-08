from tkinter import *

class Pacman:

    def __init__(self, raiz):

        self.canvas=Canvas(raiz, height=400, width=400,
            takefocus=1, bg='deepskyblue',
            highlightthickness=50)
        #Associa cada tecla direcional do teclado a um metodo da classe Pacman que eh o event handler
        self.canvas.bind('<Left>', self.esquerda)
        self.canvas.bind('<Right>', self.direita)
        self.canvas.bind('<Up>', self.cima)
        self.canvas.bind('<Down>', self.baixo)
        self.canvas.focus_force()
        self.canvas.pack()

        # Desenho da carinha----------------------------------
        self.canvas.create_oval(90, 90, 110, 110, #Criacao da cabeca
            tag='bola', fill='green')
        self.canvas.create_oval(93, 100, 98, 95, #Criacao do olho esquerdo
            tag='bola', fill='yellow')
        self.canvas.create_oval(102, 100, 107, 95, #Criacao do olho direito
            tag='bola', fill='blue')
        self.canvas.create_arc(92, 87, 108, 107, tag='bola', #Criacao da boca
            start=220, extent=100, style=ARC)
        # Fim do desenho da carinha----------------------------

    def esquerda(self, event): self.canvas.move('bola', -10, 0)
    def direita(self, event): self.canvas.move('bola', 10, 0)
    def cima(self, event): self.canvas.move('bola', 0, -10)
    def baixo(self, event): self.canvas.move('bola', 0, 10)

instancia=Tk()
Pacman(instancia)
instancia.mainloop()