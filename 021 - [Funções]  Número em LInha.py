#021 - Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e 
# imprima até a n-ésima linha.

def numero(num):
    for i in range(1, num+1):
        for j in range(i):
            print(i, end=' ')
        print()
    return 'Programa Encerrado.'

num = int(input('Número: '))
print(numero(num))
    