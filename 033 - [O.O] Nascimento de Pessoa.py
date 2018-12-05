#033 - Faça um programa orientado a objeto que peça o ano de nascimento de uma pessoa.

class Pessoa:
    nome = None
    idade = None

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def anoNasc(self):
        return anoAtual - self.idade

nome = input('Nome: ').upper()
anoAtual = int(input('Ano Corrente: '))
idade = int(input('Idade: '))

pessoa = Pessoa(nome, idade)
print('{} nasceu no ano de {}'.format(nome, pessoa.anoNasc()))