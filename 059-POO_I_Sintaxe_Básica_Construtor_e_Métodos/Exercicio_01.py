"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self):
        self.lado = 0

    def MudaLado(self, l):
        self.lado = l
        print(l)
    def RetornaLado(self):
        return self.lado

    def CalcularArea(self):
        return self.lado**2
    

quad = Quadrado

