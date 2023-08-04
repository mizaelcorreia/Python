from tkinter import *
class Packing:
    def __init__(self,instancia_Tk):
        self.container1=Frame(instancia_Tk)
        self.container2=Frame(instancia_Tk)
        self.container3=Frame(instancia_Tk)
        self.container1.pack()
        self.container2.pack()
        self.container3.pack()
        
        self.b1=Button(self.container3,text='B1')
        self.b2=Button(self.container2,text='B2')
        self.b3=Button(self.container2,text='B3')
        self.b4=Button(self.container1,text='B4')
        self.b5=Button(self.container1,text='B5')
        self.b6=Button(self.container1,text='B6')
        self.b6.pack(side=RIGHT)
        self.b4.pack(side=RIGHT)
        self.b5.pack(side=RIGHT)
        self.b2.pack(side=LEFT)
        self.b3.pack(side=LEFT)
        self.b1.pack()

raiz=Tk()
Packing(raiz)
raiz.mainloop()