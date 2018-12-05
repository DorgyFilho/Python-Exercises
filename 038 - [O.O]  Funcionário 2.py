#038- Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
# Exemplo de uso:
#   harry=funcionário("Harry",25000)
#   harry.aumentarSalario(10)

class Funcionario:

    nome = None
    salario = None
    tax = None

    def __init__(self, nome, salario, tax):
        self.nome = nome
        self.salario = salario
        self.tax = tax

    def nomeFunc(self):
        return self.nome

    def Salario(self):
        return self.salario

    def IncSalario(self):
        self.perc = (self.tax/100)
        incSal = self.perc*self.salario
        novoSalario = self.salario + incSal
        self.novoSalario = novoSalario
        return self.novoSalario
    
nome = input('Nome: ').upper()
salario = float(input('Salário: '))
tax = float(input('Taxa de aumento de salário: '))
Func = Funcionario(nome, salario, tax)
print('O(a) funcionário(a) {} recebe o salário de R${:.2f}'.format(Func.nomeFunc(), Func.Salario()))
print('Após 1 ano, ele(a) receberá um salário de R${:.2f}'.format(Func.IncSalario()))


        