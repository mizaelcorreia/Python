# -*- coding: cp1252 -*-
from tkinter import *

class Janela:

    def __init__(self,toplevel):
        self.frame=Frame(toplevel) # Cria o Frame que é o container maior
        self.frame.pack()
        self.frame2=Frame(toplevel)
        self.frame2.pack()
        
        self.titulo=Label(self.frame,text='VIDENTE 2023', #Bota a etiqueta que é o titulo
            font=('Verdana','13','bold')) # Coloca uma fonte diferente, maior e negrito
        self.titulo.pack()
        
        self.msg=Label(self.frame,width=40,height=6, #
        text = 'Adivinho o evento ocorrido!')
        self.msg.focus_force() # Ainda nao entendi
        self.msg.pack()
        
        # Definindo o botão 1
        self.b01=Button(self.frame2,text='Botão 1') # O botao 1 eh indentado
        self.b01['padx'],self.b01['pady'] = 10, 5 # É definido o tamanho do botao
        self.b01['bg']='deepskyblue' # É definida a cor de fundo do botao
        self.b01.bind("<Return>",self.keypress01) # Quando aperta o 'enter' esse objeto é chamado
        self.b01.bind("<Any-Button>",self.button01) # Quando aperta qualquer tecla esse objeto é chamado
        self.b01.bind("<FocusIn>",self.fin01) # 
        self.b01.bind("<FocusOut>",self.fout01)
        self.b01['relief']=FLAT # Define o estilo do botao
        self.b01.pack(side=LEFT) # Alinha o botao1 a esquerda dentro do FRAME
        
        # Definindo o botão 2
        self.b02=Button(self.frame2,text='Botão 2') # O botao 2 eh indentado
        self.b02['padx'],self.b02['pady'] = 10, 5 # É definido o tamanho do botao
        self.b02['bg']='deepskyblue' # É definida a cor de fundo do botao
        self.b02.bind("<Return>",self.keypress02) # Quando aperta o 'enter' esse objeto é chamado
        self.b02.bind("<Any-Button>",self.button02) # Quando aperta qualquer tecla esse objeto é chamado
        self.b02.bind("<FocusIn>",self.fin02)
        self.b02.bind("<FocusOut>",self.fout02)
        self.b02['relief']=RIDGE # Define o estilo do botao
        self.b02.pack(side=LEFT) # Alinha o botao a esquerda dentro do FRAME

    def keypress01(self,event): self.msg['text']='ENTER sobre o Botão 1' # O metodo troca a o valor da chave mensagem
    def keypress02(self,event): self.msg['text']='ENTER sobre o Botão 2' # 
    def button01(self,event): self.msg['text']='Clique sobre o Botão 1' #
    def button02(self,event): self.msg['text']='Clique sobre o Botão 2' #
    def fin01(self,event): self.b01['relief']=FLAT
    def fout01(self,event): self.b01['relief']=RIDGE
    def fin02(self,event): self.b02['relief']=FLAT
    def fout02(self,event): self.b02['relief']=RIDGE

raiz=Tk()
Janela(raiz)
raiz.mainloop()
