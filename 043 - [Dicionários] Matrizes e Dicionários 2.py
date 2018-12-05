#043 - Fazer um programa que efetua a multiplicação
#de duas matrizes de valores inteiros.
#O programa deve ler o numero de linhas e colunas de
#cada matriz e gerar valores aleatórios para estas.
#Ao final, o programa deve imprimir as matrizes originais
#e a matriz com a multiplicação das duas anteriores.
 
#1 - Importe a biblioteca random
import random
 
#2 - Crie dois dicionários vazios chamados matriz1 e matriz2
m1 = {}
m2 = {}
mRes = {}
 
#3 - Digite os valores das linhas e colunas das matrizes. Em seguida, verifique se
#o número de colunas da matriz1 é igual ao número de linhas da matriz2.
l1 = int(input('Digite o número de linhas da matriz 1: '))
c1 = int(input('Digite o número de colunas da matriz 1: '))
l2 = int(input('Digite o número de linhas da matriz 2: '))
c2 = int(input('Digite o número de colunas da matriz 2: '))
 
if c1 != l2: #Se for diferente...
    print('Matriz Inválida!!! Programa Encerrado!!!') #...o programa encerra.
else: #Caso seja igual...
 
#4 - Crie loopings para cada matriz. Em cada uma delas, acione o recurso randint da biblioteca random para gerar os elementos
#das matrizes.
    for l in range(1, l1+1):
        for c in range(1,c1+1):
            elem1 = random.randint(1,10)
        m1[(l,c)] = elem1
    print(m1, end='\t')
 
    for l in range(1,l2+1):
        for c in range(1,c2+1):
            elem2 = random.randint(1,10)
        m2[(l,c)] = elem2
    print(m2, end='\t')
 
print('\n')
 
#5 - Crie um looping for para percorrer a matriz 1 e em seguida, multiplique ambas as matrizes e armazene os resultados na
#matriz resultante.
for key in m1:
    key = (m1[key]*m2[key])
    mRes[(l,c)] = key
    print('Matriz Resultante: {}'.format(mRes, end='\t'))
print()