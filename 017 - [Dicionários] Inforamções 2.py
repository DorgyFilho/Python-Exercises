#017 - Crie um dicionário d e coloque nele seus
#dados: nome, idade, telefone,endereço.
#• Usando o dicionário d criado
#anteriormente, imprima seu nome.

agenda = {}
nome = input('Nome: ').upper()
idade = int(input('Idade: '))
endereco = input('Endereço: ').upper()
telefone = input('Telefone: ')
agenda = {'Nome': nome, 'Idade': idade, 'Endereço': endereco, 'Telefone': telefone}
print(agenda['Nome'])
