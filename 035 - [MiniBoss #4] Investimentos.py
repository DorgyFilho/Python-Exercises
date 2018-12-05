#035 - Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
# com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial
# como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
# Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class Investimento:
    nome = None
    numero = None
    saldo = None
    taxJur = None

    def __init__(self, nome, num, sdo, tax):
        self.nome = nome
        self.numero = num
        self.saldo = sdo
        self.taxJur = tax
    
    def saldo(self):
        return self.saldo

    def addJur(self):
        self.saldo += (self.taxJur/100)*self.saldo
        return 'O novo valor é {:.2f}'.format(self.saldo)

nome = input('Nome: ').upper()
num = input('Conta: ')
saldo = float(input('Digite seu valor em R$: '))
tax = float(input('Digite a taxa de Juros: '))

INV = Investimento(nome, num, saldo, tax)
print(INV.addJur())
print(INV.addJur())
print(INV.addJur())
print(INV.addJur())
print(INV.addJur())
