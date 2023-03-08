
class ValorRepetidoErro(Exception):
    def __init__(self, n):
        self.num = n
    def __str__(self):
        return 'Putz meu caro, você já digitou esse %i antes'%self.num

def main(): # Função principal.
    lista = [] # Lista vazia criada.

    for i in range(3): #
        while True:
            try:
                num = int(input('Escolher um número: '))
                break # Quando o numero digitado é corretamente um int.
            except ValueError: # Quando é encontrado um erro de valor no bloco try o except é executado. 
                print('Digite apenas números!')

        if num not in lista: # Se o numero não estiver na lista. 
            lista.append(num) # o numero é adicionado a lista.
        else:
            raise ValorRepetidoErro(num) # A exceção é invocada nesse momento chamando classe e passando como argumento o numero digitado.
        
        


if __name__ == '__main__': # Esse bloco só sera executado se esse arquivo for executado individualmente, quando outro arquivo importa o arquivo que contem esse bloco, ele não é executado.
    main()
