#096 - Write a Python program to multiplies all the items in a list.

lista = list(range(1,6))
valor = 1
for x in lista:
    valor *= x
print('O resultado da multiplicação da lista é {}'.format(valor))
