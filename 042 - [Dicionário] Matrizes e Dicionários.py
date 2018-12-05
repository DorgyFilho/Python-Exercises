#042 - Elabore um programa que preencha
#uma matriz 4 X 4 de inteiros e em
#seguida gere uma lista com a média
#aritmética de cada uma das linhas da
#matriz. Escrever a matriz completa e o
#conteúdo da lista com as médias.
 
#1 - Crie uma lista e um dicionários denominados, respectivamente, de media e matriz, cujo valor de cada um seja vazio.
matriz = {}
medias = []
 
#2 - Crie um for para percorrer o intervalo até 5, que contemplará até 4.
for l in range(1,5):
    #2.b - Crie um for para percorrer o intervalo de colunas até 5, contemplano até 4.
    for c in range(1,5):
        elem = int(input('Digite o elemento da posição {},{}: '.format(l,c)))
        matriz[(l,c)] = elem #Armazena na matriz[(l,c)]
 
#3 - Crie dois looping for, para linhas e colunas, que tenham como objetivo a realização da soma e posteriormente, calcule a
#média por 4.0 e armazene a média na lista de médias.
for l in range(1,5): #Contemplará o intervalo até 4,pois o último elemento (5) não entra na contagem.
    soma = 0 #Crie a variável soma para acumular os valores que, ao serem somados, o resultado será usado para calcular a média.
    for c in range(1,5): #Contemplará o intervalo até 4,pois o último elemento (5) não entra na contagem.
        soma += matriz[(l,c)] #Variável acumuladora.
    media = soma/4.0 #Cálculo da média.
    medias.append(media) #Armazenar a média na lista.
 
#4 - Crie um looping for que passe pela matriz.
for l in range(1,5): #Passe um for no dicionário da matriz.
    for c in range(1,5): #Percorra os elementos da matriz.
        print(matriz[(l,c)], end='\t') #Imprima em formato de matriz.
    print() #Dá enter em cada linha para gerar o formato da matriz.
 
#5 - Crie um for para percorrer a lista das médias
for elem in medias: #Percorre a lista de médias
    print(elem, end='\t') #o \t serve para imprimir lado a lado.