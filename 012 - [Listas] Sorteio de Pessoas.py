#012 - Crie uma lista com o nome de 10 pessoas, embaralhe esta lista e sorteie uma
#pessoa, depois embaralhe novamente e sorteie outra pessoa, lembrando que
#não poderá ser a mesma pessoa a ser sorteada.

import random

nomes = ['Dorgival', 'Cecilia', 'Daniella', 'Yasmmin', 'Rebeca', 'Juliana', 'Jonathas', 'Hewerton', 'Renato', 'Eliel']
sorteados = []

random.shuffle(nomes)
for i in range(len(nomes)):
    if len(nomes) > 0:
        random.shuffle(nomes)
        ganhador = random.choice(nomes)
        sorteado = nomes.pop(0)
        sorteados.append(sorteado)
    
    if len(nomes) < 0:
        print('Sorteio Encerrado.')
        break
    
    print('\n')
    print('Sorteado(a)')
    print(sorteado)
    print('='*10)
    for i in range(len(nomes)):
        print(nomes[i])
    print('='*10)
    print(sorteados)