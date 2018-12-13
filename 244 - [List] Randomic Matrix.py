#249 - Faça um programa que crie uma matriz aleatoriamente.
#O tamanho da matriz deve ser informado pelo usuário.

import random

matrix = []

lin = int(input('Line: '))
col = int(input('Column: '))

for l in range(lin):
    line = []
    for c in range(col):
        pair = random.randint(0,9)
        result = f'{pair}'
        line.append(result)
    matrix.append(line)

for a in matrix:
    for b in a:
        print(b, end=' ')
    print()