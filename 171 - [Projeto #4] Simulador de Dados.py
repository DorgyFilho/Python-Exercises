#171 - Simule um jogo de dados.

import random

op = True
while op == True:
    for i in range(1):
        print('O Número Sorteado é {}'.format(random.randint(1,6)))
    print('\n')
    print('Deseja Jogar de Novo? Digite S para Sim ou N para Não')
    opcao = input('Digite a sua resposta: ').upper()
    if opcao == 'N':
        op = False
        print('Jogo Encerrado.')
        break

