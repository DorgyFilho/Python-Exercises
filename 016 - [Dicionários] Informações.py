#016 - Crie um dicionário que é uma agenda e
# coloque nele os seguintes dados: chave (cpf),
# nome, idade, telefone. O programa deve ler
# um número indeterminado de dados, criar a
# agenda e imprimir todos os itens do
# dicionário no formato chave: nome-idade-fone.

agenda = {}
cpf = ''
while cpf != 0:
    cpf = int(input('CPF: '))
    if cpf == 0:
        print('Cadastramento Encerrado.')
    else:
        nome = input('Nome: ').upper()
        idade = int(input('Idade: '))
        fone = input('Telefone: ')
        agenda[cpf] = {'Nome': nome, 'Idade': idade, 'Telefone': fone}
print(agenda)