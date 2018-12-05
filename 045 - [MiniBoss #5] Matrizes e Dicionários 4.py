#045 - Elabore um algoritmo que preencha
#uma matriz 4 X 4 de inteiros e depois
#faça:
#Imprimir toda a matriz.
#Trocar a segunda linha pela terceira.
#Trocar a primeira pela quarta coluna.
#Imprimir novamente a matriz
 
#1 - Crie um dicionário denominado 'matriz', cujo valor seja vazio.
matriz = {}
 
#2 - Crie um looping for para digitar os elementos da matriz 4 x 4.
for l in range(1,5): #Coloco o 5, mas contemplará até o 4.
    for c in range(1,5):
        elem = int(input('Digite o elemento na posição {}, {}: '.format(l,c)))
    matriz[(l,c)] = elem
print(matriz)
print('\n')
 
#3 - Realize a troca da segunda linha pela terceira linha.
matriz[2,c] = matriz[3,c]
matriz[l,1] = matriz[l,4]
 
#4 - Imprima a matriz novamente.
print(matriz)