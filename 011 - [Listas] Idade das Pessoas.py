#011 - Escreva um programa em Python que:
# a. Solicita ao usuário o nome e a idade de 20 pessoas e os armazena em uma ou
# duas listas;
# b. Após ler e guardar todos os nomes e idades, o seu programa deverá ficar
# executando e solicitar que o usuário informe o nome de uma pessoa;
# c. Quando o usuário digitar o nome da pessoa e o nome dela estiver na lista, seu
# programa deverá imprimir “A idade dela é X anos”, onde X é a idade armazenada
# na lista anteriormente. Lembre-se de converter as duas strings para minúsculas
# antes de comparar;
# d. Caso o nome da pessoa não esteja na lista, o seu programa deverá imprimir
# “Pessoa não encontrada”;
# e. Se o usuário digitar o nome “fim” seu programa deve parar de executar. Enquanto
# isso não ocorrer, seu programa deverá ficar executando.

lNome = []
lIdade = []

for i in range(1, 4):
    nome = input('Nome: ').upper()
    idade = input('Idade: ')
    lNome.append(nome)
    lIdade.append(idade)

while True:
    busca = input('Nome a ser buscado: ').upper()
    if busca == 'FIM':
        print('Busca encerrada.')
        break
    else:
        if busca in lNome:
            refIdade = lNome.index(busca)
            print('A sua idade é {} anos'.format(lIdade[refIdade]))
        else:
            print('Pessoa não encontrada.')
