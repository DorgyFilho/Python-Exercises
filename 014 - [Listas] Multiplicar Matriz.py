#014 -Faça um programa que leia duas matrizes do usuário e faça a multiplicação entre
#elas. 

matriz = []
lin = int(input('Linhas: '))
col = int(input('Colunas: '))

for l in range(1, lin+1):
    linha = []
    for c in range(1, col+1):
        pos = int(input('Posição {}, {}: '.format(l,c)))
        linha.append(pos)
    matriz.append(linha)

for a in matriz:
    for b in a:
        novaMatriz = 2*b
        print(novaMatriz, end=' ')
    print()