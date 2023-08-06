from tkinter import *

class Linhas:

    def __init__(self,raiz):
        #Nem o Canvas esta no Frame e nem o Frame esta no Canvas
        self.canvas = Canvas(raiz, width=400, height=400,
                            cursor='circle', bd=5)
        self.canvas.pack()
        self.frame=Frame(raiz)
        self.frame.pack()
        
        self.last=[200,200] # Posição inicial inicial para começar o desenho
        
        # Configuração geral que será usada pelos botoes
        configs={'fg':'darkblue', 'bg':'ghostwhite', 'relief':RIDGE,
                'width':11,'font':('Verdana','8','bold')}
        
        #Botao que vai para a esquerda dentro do Canva, chama o metodo left
        self.b1=Button(self.frame, configs,
                text='Esquerda', command=self.left) 
        self.b1.pack(side=LEFT)
        
        #Botao que vai para a cima dentro do Canva, chama o metodo up
        self.b2=Button(self.frame, configs,
                text='Para cima', command=self.up)
        self.b2.pack(side=LEFT)
        
        #Botao que vai para baixo dentro do Canva, chama o metodo down
        self.b3=Button(self.frame, configs,
                text='Para baixo', command=self.down)
        self.b3.pack(side=LEFT)
        
        #Botao que vai para a direita dentro do Canva, chama o metodo right
        self.b4=Button(self.frame, configs,
                text='Direita', command=self.right)
        self.b4.pack(side=LEFT)

    def left(self): # Desenha um segmento para a esquerda

        x, y = self.last[0]-10, self.last[1]
        self.canvas.create_line(self.last, x, y, fill='red')
        self.last=[x,y]

    def up(self): # Desenha um segmento para cima

        x, y = self.last[0], self.last[1]-10
        self.canvas.create_line(self.last, x, y, fill='black')
        self.last=[x,y]

    def down(self): # Desenha um segmento para baixo

        x, y = self.last[0], self.last[1]+10
        self.canvas.create_line(self.last, x, y, fill='blue')
        self.last=[x,y]

    def right(self): # Desenha um segmento para a direita

        x, y = self.last[0]+10, self.last[1]
        self.canvas.create_line(self.last, x, y, fill='purple')
        self.last=[x,y]

instancia=Tk()
Linhas(instancia)
instancia.mainloop()