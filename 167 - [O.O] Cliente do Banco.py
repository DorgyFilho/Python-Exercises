#167 - Exercício 10.12 - Nilo Menezes: Página 230

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
class Conta:
    def __init__(self, cliente, numero, saldo):
        self.saldo = 0
        self.cliente = cliente
        self.numero = numero
        self.operacao = []
        self.depositar(saldo)

    def resumo(self):
        print('Conta: {}\nSaldo:R${:.2f}'.format(self.numero, self.saldo))
    
    def pode_sacar(self, valor):
        return self.saldo >= valor

    def sacar(self, valor):
        if self.pode_sacar(valor):
            self.saldo -= valor
            self.operacao.append(['SAQUE', valor])
            return True
        else:
            print('Saldo Insuficiente.')
            return False
    
    def depositar(self, valor):
        self.saldo += valor
        self.operacao.append(['DEPÓSITO', valor])
    
    def extrato(self):
        for op in self.operacao:
            print('Operação: {}\nValor: R${:.2f}\n'.format(op[0], op[1]))

class ContaEspecial(Conta):
    def __init__(self, cliente, numero, saldo, limite=0):
        Conta.__init__(self, cliente, numero, saldo)
        self.limite = limite

    def pode_sacar(self, valor):
        return self.limite + self.saldo >= valor
    
    def ext(self):
        Conta.extrato(self)
        print('Limite: R${:.2f}\nDisponível: R${:.2f}'.format(self.limite, self.limite + self.saldo))

Dorgival = Cliente('Dorgival Filho', '1234-5678')
Conta2 = ContaEspecial([Dorgival], '1234', 5000, 1000)
Conta2.sacar(1000)
Conta2.sacar(1000)
Conta2.ext()




