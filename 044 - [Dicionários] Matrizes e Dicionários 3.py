#044 - Faça um algoritmo que preencha uma
#matriz 3 X 3 de inteiros e escreva:
#– A matriz completa
#– A soma dos números ímpares da matriz
#– A soma dos números pares da matriz
 
#1 - Crie um dicionário denominado 'matriz', cujo valor é vazio. Além disso, crie duas listas denominadas 'somaPar' e 'somaImpar,
#cujo calor de cada um seja vazio.
matriz = {}
somaImpar = []
somaPar = []
 
#2 - Crie um for que percorra um intervalo até 4, pois contemplará até o 3 para as linhas.
for l in range(1,4):
    #2.b - Crie um for que faça o mesmo para as colunas
    for c in range(1,4):
        elem = int(input('Digite o elemento da posição {}, {}: '.format(l,c)))
        #Armazene os valores digitados na matriz(dicionário)
        matriz[(l,c)] = elem
 
#3 - Crie um elemento for para percorrer o intervalo dado no passo anterior para as linhas e colunas.
#Porém, agora será necessária a criação de duas variáveis denominadas 'somaPares' e 'somaImpares',
#cujo valor inicial de cada um será zero. Depois, faça a soma de cada uma.
for l in range(1,4):
    somaPares = 0
    somaImpares = 0
    for c in range(1,4):
        if matriz[(l,c)]%2 == 0:
            somaPares += matriz[(l,c)]
        else:
            somaImpares += matriz[(l,c)]
    somaPar.append(somaPares)
    somaImpar.append(somaImpares)
 
#4 - Agora, mostre a matriz inteira e em seguida, mostre a soma dos pares e dos ímpares.
for l in range(1,4):
    for c in range(1,4):
        print(matriz[(l,c)], end= '\t') #Quero lado a lado.
    print() #Dá enter em cada linha.
 
somaP = sum(somaPar)
somaI = sum(somaImpar)
print('Soma dos Pares: {} --> Soma dos Ímpares: {}'.format(somaP, somaI))