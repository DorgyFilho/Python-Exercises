#018 - 3. Crie um programa que cadastre
# informações de várias pessoas (nome,
# idade e cpf) e depois coloque em um
# dicionário. Depois remova todas as
# pessoas menores de 18 anos do
# dicionário e coloque em outro dicionário. 

agenda = {}
cpf = ''
while cpf != '0':
    cpf = input('CPF: ')    
    if cpf == '0':
        print('Cadastramento Encerrado.')
        print('='*20)
        break
    nome = input('Nome: ').upper()
    idade = int(input('Idade: '))
    agenda[cpf] = {'Nome': nome, 'Idade': idade}

cpfMenores = {}
listaMenores = []
for chave in agenda:
    if agenda[chave]['Idade'] < 18:
        listaMenores.append(chave)

for cpf in listaMenores:
    cpfMenores[cpf] = agenda.pop(cpf)

print('='*10)
print('Agenda: ')
for cpf in agenda:
    print('CPF: {}, Nome: {}, Idade:{}'.format(cpf, agenda[cpf]['Nome'], agenda[cpf]['Idade']))

print('='*10)
print('Menores: ')
for cpf in cpfMenores:
    print('CPF: {}, Nome: {}, Idade: {}'.format(cpf, cpfMenores[cpf]['Nome'], cpfMenores[cpf]['Idade']))
    