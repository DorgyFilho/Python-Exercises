#013 - Faça um programa que crie uma matriz aleatoriamente e guarde em uma lista. As
# dimensões da matriz deverão ser informadas pelo usuário. O programa deverá
# imprimir a matriz criada na tela, no formato m x n. Ex:
# Matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Exibir na tela:
# 1 2 3
# 4 5 6
# 7 8 9

m = []
lin = int(input('Linhas: '))
col = int(input('Colunas: '))

for l in range(1, lin+1):
    linha = []
    for c in range(1, col+1):
        pos = int(input('Posição {}, {}: '.format(l,c)))
        linha.append(pos)
    m.append(linha)

for a in m:
    for b in a:
        print(b, end=' ')
    print()