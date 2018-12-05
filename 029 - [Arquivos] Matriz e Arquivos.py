#029 - Crie um programa que leia uma matriz 3x3 do usuário e guarde os valores em uma
# arquivo, na forma de matriz:
# Ex: 
# 1 2 3
# 4 5 6
# 7 8 9

arq = open('/home/dorginho/matriz.txt', 'w')
matriz = []

for l in range(1, 4):
    linha = []
    for c in range(1,4):
        pos = int(input('Posiçao {},{}: '.format(l,c)))
        linha.append(pos)
    matriz.append(linha)

for a in matriz:
    for b in a:
        arq.writelines(str(b))
        arq.writelines(' ')
    arq.writelines('\n')

arq.close()

