from tkinter import *
class SPFC:
    
    def __init__(self,raiz):

        self.canvas=Canvas(raiz, width=200, height=200, bg='dodgerblue')
        self.canvas.pack()
        
        altura = 200 # Altura do canvas
        
        pol=self.canvas.create_polygon # Cria um poligono genérico
        
        ret=self.canvas.create_rectangle # Cria um retangulo genérico
        
        # Desenha o contorno do escudo e pinta de branco por dentro
        pol(100, altura-10,
            10, altura-145,
            10, altura-190,
            190, altura-190,
            190, altura-145,
            100, altura-10, fill='white')
        
        # Desenha o retangulo onde fica escrito SPFC e pinta de preto por dentro, 
        # que fica dentro do poligono desenhado anteriormente
        ret(15, altura-150, 185, altura-185, fill='black')
        
        # Desenha o triangulo vermelho e pinta de vermelho por dentro, que fica dentro do poligono pintado de branco
        pol(20, altura-140,
            95, altura-140,
            95, altura-30,
            20, altura-140, fill='red')
        
        # Desenha o triangulo triangulo da direita, depois preenche da cor preta por dentro, que fica dentro do poligono 
        # pintado de branco 
        pol(105, altura-30,
            105, altura-140,
            180, altura-140,
            105, altura-30, fill='black')
        
        #Escreve SPFC no escudo do clube
        self.canvas.create_text(100, altura-167.5, text='S P F C',
            font=('Arial','26','bold'),
            anchor=CENTER, fill='white')

instancia=Tk()
SPFC(instancia)
instancia.mainloop()