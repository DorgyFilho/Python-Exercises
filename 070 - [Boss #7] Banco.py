#070 - Faça um programa que simule uma conta bancária por meio de Orientação a Objeto.
#Obs: Utilize as bibliotecas datetime e pytz para registrar o momento da transação bancária.

import datetime
import pytz

class Conta:

    #Data e hora das transações bancárias
    @staticmethod #Registrará os horários da transação bancária
    def horaAtual(): #Mostrará a hora no fuso horário local.
        hora = datetime.datetime.utcnow()
        return pytz.utc.localize(hora)
    
    nome = None
    saldo = None

    #Criar a conta bancária    
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.Ocorrencia = []
        print('Conta criada com sucesso para {}'.format(self.nome))
    
    #Adicionar saldo.
    def credito(self, valor):
        if self.saldo >= 0: #Adicionar saldo.
            self.saldo += valor
            self.mostrarSaldo() #Relatório sobre o saldo.
            self.Ocorrencia.append((Conta.horaAtual(), valor))
    
    #Retirar saldo.
    def debito(self, valor):
        if 0 < valor <= self.saldo: #Retirar saldo.
            self.saldo -= valor
            self.Ocorrencia.append((Conta.horaAtual(), -valor))
        else:
            print('Escolha um valor maior que zero ou menor/igual ao saldo.')
        self.mostrarSaldo()
    
    #Extrato.
    def mostrarSaldo(self):
        return 'O saldo do(a) cliente {} é R${:.2f}'.format(self.nome, self.saldo)

    #Detalhes da transação.
    def mostrarOcorrencia(self):
        for data, valor in self.Ocorrencia:
            if valor > 0:
                operacao = 'Creditado'
            elif valor == 0:
                operacao = 'Mantido' 
            else:
                operacao = 'Sacado'
                valor *= - 1
            return 'Valor de R${:.2f} {} na data {} às {} no horário local'.format(self.saldo, operacao, data, data.astimezone())

#PROGRAMA PRINCIPAL
nome = input('Nome: ').upper()
saldo = float(input('Digite o seu saldo: '))
cliente = Conta(nome, saldo)
print(cliente.mostrarSaldo())
repetir = 'S'
while repetir == 'S':
    print('Escolha uma operação\n1-Creditar\n2-Sacar\n3-Sair')
    op = input('Digite sua resposta: ')
    if op == '1':
        cliente.credito(int(input('Valor a ser creditado: ')))
        cliente.mostrarOcorrencia()
        print(cliente.mostrarSaldo()) 
    elif op == '2':
        cliente.debito(int(input('Valor a ser sacado: '))) 
        cliente.mostrarOcorrencia()
        print(cliente.mostrarSaldo())
    elif op == '3':
        print('Fim da operação')
    print('Deseja repetir a operação?\nS-Sim\nN-Não')
    repetir = input('Digite a sua resposta: ').upper()
    if repetir == 'N':
        print('Operação Encerrada. Obrigado(a) e Volte Sempre.')
        break  

            

