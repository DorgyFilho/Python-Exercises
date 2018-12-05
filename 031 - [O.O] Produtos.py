#031 - Construa uma classe Produto, que deve ter
#os atributos codigo e preco (privados).
#Adicione também um atributo estático
#qtdProd, que deverá ser acrescentado toda
#vez que um novo objeto é criado.
#Crie os métodos get e set e teste a classe.

class Produto:
    prod = None
    __preco = None
    __cod = None
    qtdProd = 0

    def __init__(self, prod, preco, cod, qtdProd):
        self.prod = prod
        self.__preco = preco
        self.__cod = cod
        self.qtdProd = qtdProd
    
    def getProd(self):
        return self.prod
    
    def setProd(self):
        self.qtdProd += 1
        return 'O estoque possui {} produtos.'.format(self.qtdProd)
    
qtdProd = 0
while True:
    prod = input('Produto: ').upper()
    if prod == 'FIM':
        print('Programa Encerrado.')
        break
    else:
        preco = float(input('Preço: '))
        cod = input('Código: ')
        Prod = Produto(prod, cod, preco, qtdProd)
        print(Prod.setProd())
        qtdProd += 1