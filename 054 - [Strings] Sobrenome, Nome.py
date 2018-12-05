#66 - Implemente um programa que receba um nome e apresente apenas o último nome e o 1o nome na
#seguinte forma: Último nome, 1o nome
#Exemplo:
#Manuel Francisco Teixeira Duarte
#Duarte, Manuel

#1 - Digite o seu nome completo.
nCom = input('Digite o seu nome completo: ')

#2 - Utilize o recurso split() para remover o espaço
nome = nCom.split()

#3 - Leia o tamanho do nome digitado com o len()
qtd = len(nome)

#4 - Estabeleça condições para a quantidade de nomes.
if qtd > 1: #Sobrenome, Nome
    print('{}, {}'.format(nome[-1], nome[0]))
elif qtd > 2: #Sobrenome Sobrenome, Nome
    print('{} {},{}'.format(nome[-2], nome[-1], nome[0]))
else: #Nome completo.
    print(nCom)