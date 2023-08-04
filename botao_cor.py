from tkinter import *

class Janela:
    def __init__(self,toplevel):
        self.frame=Frame(toplevel) #Cria o Frame Master
        self.frame.pack() # Empacota pelo gerenciador grafico
     
        self.texto=Label(self.frame, text='Clique para ficar amarelo') #Cria a etiqueta com o texto
        self.texto['width']=26 # Da a largura do texto
        self.texto['height']=3 # Da a altura do texto
        self.texto.pack() # Empacota pelo gerenciador grafico
     
        self.botaoverde=Button(self.frame,text='Clique') # Cria o botao que se chama botao verde com o texto dentro
        self.botaoverde['background']='green' # Define a cor de fundo do botao como sendo verde
        self.botaoverde.bind("<Button-1>",self.muda_cor) # Ao clicar com o botao esquerdo do mouse o metodo muda_cor é chamado
        self.botaoverde.pack() # O botao é empacotado pelo gerenciador grafico
    
    def muda_cor(self, event): # Classe que recebe o evento clicar no mouse
        # Muda a cor do botao!
        if self.botaoverde['bg']=='green': #Se a cor de fundo do botao for verde
            self.botaoverde['bg']='yellow' # Atualiza a cor do botao para amarelo
            self.texto['text']='Clique para ficar verde' # Atualiza a o texto da etiqueta
        else: # Quando o botao nao é verde, no caso em que é amarelo
            self.botaoverde['bg']='green' # A cor atribuida ao botao passa a ser verde
            self.texto['text']='Clique para ficar amarelo' # Ficando o botando verde a label é atualizada para dizer para clicar no botao e ele ficar

raiz=Tk()
Janela(raiz)
raiz.mainloop()