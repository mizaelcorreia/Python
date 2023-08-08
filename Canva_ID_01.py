# -*- coding: cp1252 -*-
from tkinter import *
from time import localtime

class Horas:

    def __init__(self,raiz):
        
        self.canvas=Canvas(raiz, width=200, height=100)
        self.canvas.pack()
        self.frame=Frame(raiz)
        self.frame.pack()
        
        self.altura = 100 # Altura do canvas
        
        # Desenho do relógio-----------------------------
        pol=self.canvas.create_polygon
        ret=self.canvas.create_rectangle
        self.texto=self.canvas.create_text
        self.fonte=('Arial','20','bold')
        
        #Desenho do trapezio
        pol(10, self.altura-10,
            40, self.altura-90,
            160, self.altura-90,
            190, self.altura-10, fill='darkblue')
        
        #Parte de dentro do trapezio
        pol(18, self.altura-15,
            45, self.altura-85,
            155, self.altura-85,
            182, self.altura-15, fill='dodgerblue')
        
        #Mostrador de horas do relogio
        ret(45, self.altura-35,
            90, self.altura-60, fill='black', outline='')
        
        #Mostrador de minutos do relogio
        ret(110, self.altura-35,
            155, self.altura-60, fill='black', outline='')
        
        #Os dois pontos entre cada mostrador 
        self.texto(100, self.altura-50, text=':',
            font=self.fonte, fill='yellow')
        # Fim do desenho do relógio-----------------------
        
        self.mostrar=Button(self.frame, text='Que horas sao?',
            command=self.mostra, #Chama o metodo 'mostra'
            font=('Arial', '11', 'bold'),
            fg='darkblue', bg='white')
        self.mostrar.pack(side=LEFT)

    def mostra(self):
        
        self.canvas.delete('digitos_HORA')
        self.canvas.delete('digitos_MIN')
        
        HORA = str( localtime()[3] ) 
        MINUTO = str( localtime()[4] )
        print(HORA)
        print(MINUTO)
        
        self.texto(67.5, self.altura-50, text=HORA, fill='yellow',
            font=self.fonte, tag='digitos_HORA')
        
        self.texto(132.5, self.altura-50, text=MINUTO, fill='yellow',
            font=self.fonte, tag='digitos_MIN')

instancia=Tk()
Horas(instancia)
instancia.mainloop()