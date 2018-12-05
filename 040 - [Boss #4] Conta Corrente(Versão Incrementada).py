#040 - Considere as classes ContaCorrente e Poupanca
#apresentadas em sala de aula. Crie uma classe
#ContaImposto que herda de conta e possui um atributo
#percentualImposto. Esta classe também possui um
#método calculaImposto() que subtrai do saldo, o valor
#do próprio saldo multiplicado pelo percentual do
#imposto. Crie um programa para criar objetos, testar
#todos os métodos e exibir atributos das 3 classes
#(ContaCorrente, Poupanca e ContaImposto).

class Conta:

    numero = None
    saldo = None

    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def credito(self, valor):
        self.saldo += valor

    def debito(self, valor):
        self.saldo -= valor
    
    def impValor(self):
        return 'Saldo atual: R${:.2f}'.format(self.saldo)

class Poupanca(Conta):
    juros = None
    nSaldo = None

    def __init__(self, numero, juros, saldo):
        Conta.__init__(self, numero, saldo)
        self.juros = juros

    def rend(self):
        self.nSaldo = self.saldo + (self.saldo*(self.juros/100))
        return 'Com o rendimento calculado, o saldo agora é de R${:.2f}'.format(self.nSaldo)

class Imposto(Conta):
    taxa = None
    nValor = None

    def __init__(self, numero, taxa, saldo):
        Conta.__init__(self, numero, saldo)
        self.taxa = taxa
    
    def calculaImp(self):
        self.nValor = self.saldo - (self.saldo*(self.taxa/100))
        return 'Com a dedução, o novo saldo é de R${:.2f}'.format(self.nValor)

N = input('Conta: ')
S = float(input('Saldo Atual: '))
C = int(input('Credito: '))
D = int(input('Débito: '))
J = float(input('Juros: '))
I = float(input('Imposto: '))

R1 = Conta(N,S)
R1.credito(C)
R1.debito(D)

R2 = Poupanca(N,J,S)
R2.rend()

R3 = Imposto(N,I,S)
R3.calculaImp()

print(R1.impValor())
print('='*20)
print(R2.rend())
print('='*20)
print(R3.calculaImp())