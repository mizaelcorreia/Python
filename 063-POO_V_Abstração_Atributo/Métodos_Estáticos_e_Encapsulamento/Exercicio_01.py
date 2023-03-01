"""
Escreva um programa de bancos que possua:
    Uma classe Banco com os atributos
    - private total
    - public TaxaReserva
    - private reservaExigida

    E métodos
    - public podeFazerEmprestimo(valor) --> bool
    - public MudaTotal(valor)

E uma classe conta com os atributos
    - private saldo
    - private ID
    - private senha

    E métodos
    - public deposito(senha, valor)
    - public saque(senha, valor)
    - public podeReceberEmprestimo(valor) --> bool
    - public saldo --> float
"""

class Banco(object): #Classe Banco que herda da classe object.
    __total = 10000 #Atributo private.
    TaxaReserva = 0.1 #Atributo public.
    reservaExigida = __total*TaxaReserva # Atributo que recebe o produto de dois outros atributos, um privado e um public respectivamente.

    def podeFazerEmprestimo(valor): # Metodo que recebe valor no argumento.
        Banco.__total -= valor # Valor recebido pelo metodo podeFazerEmprestimo é subtraido do atributo privado __total da classe Banco.
        if Banco.__total >= Banco.reservaExigida: # Se o atributo private __total da classe banco tiver um valor maior ou que o atributo public da classe banco a condiçao é executada.
            pode = True
        else: #Situaçao em que o banco nao tem a reserva minima necessária pra fazer emprestimo.
            pode = False

        Banco.__total += valor # valor recebido no metodo podeFazerEmprestimo é acrescentado ao atributo  private __total da classe Banco.

        return pode # Retorna o booleano pode para o objeto que invocou o método.

    def MudaTotal(valor): # Metodo definido MudaTotal que recebe o valor do objeto instanciado a classe Banco.
        Banco.__total += valor # O valor recebido pelo metodo MudaTotal é acrescido ao atributo private __total da classe Banco.

class Conta: # Criação da classe Conta
    def __init__(self, saldo, ID, senha): # Criação do construtor que recebe os parametros objeto, saldo, ID e senha que podem ser de qualquer tipo.
        self.__saldo = saldo # Atribuição do parametro saldo ao atributo privado __saldo do objeto que foi indentado a classe Conta.
        self.__ID = ID # Atribuição do parametro ID ao atributo privado __ID do objeto que foi indentado a classe Conta.
        self.__senha = senha # Atribuição do parametro senha ao atributo privado __senha do objeto que foi indentado a classe Conta.

    def deposito(self, senha, valor): # Definição do método deposito, que recebe o objeto instanciado pela classe Conta, e os parametros senha e valor que podem ser de qualquer tipo. 
        if senha == self.__senha: # Se o parametro senha recebido da invocação do metodo for igual ao atributo private __senha do objeto instanciado pela classe Conta, a condiçao if é atendida.
            self.__saldo += valor # É acrescentado o valor recebido pelo metodo deposito ao atributo private __saldo do objeto instanciado pela classe Conta.
            Banco.mudaTotal(valor) # Da classe Banco é invocado o método mudaTotal, que recebe o parametro valor que foi o parametro recebido pelo metodo deposito

    def saque(self, senha, valor): # Definiçao do metod saque, que recebe o objeto instanciado, o atributo senha e valor que pode ser de qualquer tipo.
        if senha == self.__senha: # Se o valor recebido como argumento do metodo senha, for igual ao atributo private __senha do objeto a condição é executada
            self.__saldo -= valor # O valor recebido pelo metodo saque é subtraido do atributo private __saldo do objeto que foi indentado a classe Conta.
            Banco.mudaTotal(-valor) # A classe Banco invoca o método mudaTotal e passa como argumento o parametro valor com o sinal negativo.

    def podeReceberEmprestimo(self, valor): # Método podeReceberEmprestimo recebe o objeto instanciado na classe Conta e o valor que pode ser uma variável de qualquer tipo.
        return Banco.podeFazerEmprestimo(valor) # retorna a classe Banco acessando o método podeFazerEmprestimo com o valor como argumento.

    def saldo(self): # Definição da função saldo que recebe como argumento um objeto indentado a classe Conta
        print(self.__saldo) #Imprime do objeto indentado a classe conta o valor do atributo privace __saldo