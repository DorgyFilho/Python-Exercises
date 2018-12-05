#039 - Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, 
# saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class Conta:

    def __init__(self, nome='', numero=' ', saldo=0):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = saldo
    
    def Nome(self):
        nome = input('Digite seu nome: ').upper()
        self.__nome = nome
        return self.__nome

    def Numconta(self):
        numero = input('Número da Conta: ')
        self.__numero = numero
        return self.__numero
    
    def Saldo(self):
        saldo = float(input('Informe o seu saldo atual: '))
        return self.__saldo

    def alterarNome(self):
        nome = input('Em caso de necessidade, altere o seu nome: ').upper()
        self.__nome = nome

    def deposito(self):
        dep = int(input('Digite o valor a ser depositado: '))
        if dep >= 0:
            self.__saldo += dep
            return self.__saldo
        else:
            print('Digite apenas valores numéricos maiores que zero.')


    def saque(self):
        saque = int(input('Digite o valor a ser sacado: '))
        if saque >= 0:
            self.__saldo -= saque
            return self.__saldo
        else:
            print('Digite apenas valores numéricos.')
    
    def __repr__(self):
        return 'Status:\nNome:{}\nConta:{}\nSaldo:R${:.2f}'.format(self.__nome, self.__numero, self.__saldo)

def main():
    print('{:50}'.format('SEJA BEM-VINDO(A) AO BANCO BUFUNFA'))
    con = Conta()
    while True:
        print(con)
        print('Escolha uma das opções abaixo:\n1-Depósito\n2-Saque\n3-Cadastrar\n4-Alterar Nome\n5-Sair')
        opcao = input('Digite a sua opção: ')
        if opcao == '1':
            con.deposito()
        elif opcao == '2':
            con.saque()
        elif opcao == '3':
            con.Nome()
            con.Numconta()
        elif opcao == '4':
            con.alterarNome()
        elif opcao == '5':
            print('Fim da operação.')
            break
        else:
            print('Erro! Operação Inválida.')

main()       


    
    