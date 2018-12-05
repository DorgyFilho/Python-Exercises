#037 - Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) 
#e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos 
# para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:

    nome = None
    salario = None

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def nomeFunc(self):
        return self.nome

    def Salario(self):
        return self.salario

nome = input('Nome: ').upper()
salario = float(input('Salário: '))
Func = Funcionario(nome, salario)
print('O nome do(a) funcionário(a) é {} e o seu salário é de R${:.2f}'.format(Func.nomeFunc(), Func.Salario()))