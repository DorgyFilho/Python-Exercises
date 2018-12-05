#020 - Escreva um programa em Python para realizar as ações abaixo obedecendo a
# regra geral:
# CADASTROS:
# a. Solicita ao usuário o CPF, o nome e a idade de 20 pessoas e os armazena em um
# dicionário usando o CPF como chave. Internamente, use outro dicionário
# contendo as chaves “nome” e “idade” para melhor organização (dicionário
# aninhado);
# CONSULTAS:
# b. Após ler e guardar todas as informações, o seu programa deverá solicitar que o
# usuário informe o CPF de alguém;
# c. Quando o usuário digitar o CPF da pessoa, se ela estiver no dicionário, seu
# programa deverá imprimir “Nome: X – idade: Y anos”, onde X é o nome e Y é a
# idade que foram armazenados no dicionário anteriormente.
# d. Caso o nome da pessoa não esteja no dicionário, o seu programa deverá imprimir
# “Pessoa não encontrada”.
# e. Se o usuário digitar o CPF “0” seu programa deve parar de executar. Enquanto
# isso não ocorrer, seu programa deverá ficar executando e exibindo as informações
# das pessoas cujos CPFs foram digitados.
# Regra geral:
#  O trecho de código que busca o CPF da pessoa no dicionário e devolve a string a
# ser exibida na tela (“Nome: X – idade: Y anos”) deverá ser escrito em uma
# função. A função deve receber o dicionário e o CPF da pessoa como parâmetros e
# deve retornar:
#  a string a ser exibida na tela (não use print dentro da função) se o
# CPF existir no dicionário; ou
#  string vazia “” se o CPF da pessoa não estiver armazenado no
# dicionário.

cadastro = {}
cpf = ''
for i in range(1,21):
    cpf = input('CPF ou 0 para sair: ')
    if cpf == '0':
        print('Cadastramento Encerrado.')
    nome = input('Nome: ').upper()
    idade = int(input('Idade: '))
    cadastro[cpf] = {cpf:{'Nome': nome, 'Idade': idade}}

def buscar(cadastro):
    Cpf = cpf
    if Cpf in cadastro:
        return 'Nome: {} - Idade: {} Anos'.format(cadastro[cpf][cpf]['Nome'], cadastro[cpf][cpf]['Idade'])
    else:
        return 'Pessoa não encontrada'

while True:
    cpf = input('Digite o cpf a ser buscado: ')
    if cpf != '0':
        print(buscar(cadastro))
    else:
        print('Programa encerrado.')
        break