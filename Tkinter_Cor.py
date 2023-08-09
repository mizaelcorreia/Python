from tkinter import *

class Palheta:

    def __init__(self,raiz):
    
        raiz.title("Palheta")
        self.canvas=Canvas(raiz, width=200, height=200)
        self.canvas.pack()
        self.frame=Frame(raiz)
        self.frame.pack()
        
        #Cria o circulo de cores
        self.canvas.create_oval(15, 15, 185, 185,
        fill='white', tag='bola')
        
        #Cria a etiqueta vermelha e o campo, colocando o foco no widget desse campo
        Label(self.frame,text='Vermelho: ').pack(side=LEFT)
        self.vermelho=Entry(self.frame, width=4)
        self.vermelho.focus_force()
        self.vermelho.pack(side=LEFT)
        
        #Cria a etiqueta verde e o campo pra entrar com o valor
        Label(self.frame,text='Verde: ').pack(side=LEFT)
        self.verde=Entry(self.frame, width=4)
        self.verde.pack(side=LEFT)
        
        #Cria a etiqueta azul e o campo pra entrar com o valor
        Label(self.frame,text='Azul: ').pack(side=LEFT)
        self.azul=Entry(self.frame, width=4)
        self.azul.pack(side=LEFT)
        
        #Cria o botao e atribvui o metodo 'misturar' quando se clica no botao
        Button(self.frame, text='Mostrar',
            command=self.misturar).pack(side=LEFT)
        
        #Cria uma Label na frente do botao de tamanho 8 strings e deixa ela em branco
        self.rgb=Label(self.frame, text='', width=8,
        font=('Verdana','10','bold'))
        self.rgb.pack()
    
    def misturar(self):
        
        #Pega a cor digitada e transforma em hexadecimal
        cor="#%02x%02x%02x" %(int(self.vermelho.get()),
            int(self.verde.get()),
            int(self.azul.get()))
        
        #Apaga o desenho do canva que tem a tag bola e inicalmente tem a cor branca
        self.canvas.delete('bola')
        
        #Cria um novo circulo com a tag tambem chamada de bola e com a cor escolhida pelo usuario da combinacao 
        #RGB e transformada em hexadecimal
        self.canvas.create_oval(15, 15, 185, 185,
            fill=cor, tag='bola')
        
        #Diz qual é o codigo hexadecimal da cor e volta o foco pro primeiro entry
        self.rgb['text'] = cor
        self.vermelho.focus_force()

inst = Tk()
Palheta(inst)
inst.mainloop()