#021 - Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função 
# que receba um valor n inteiro imprima até a n-ésima linha.

def numero(num):
    for i in range(1, num+1):
        for j in range(1, i):
            print(j, end=' ')
        print()
    return 'Programa Encerrado.'

num = int(input('Número: '))
print(numero(num))