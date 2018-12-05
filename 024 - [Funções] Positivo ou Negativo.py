#024 - Faça um programa, com uma função que necessite de um argumento. A função retorna o valor 
# de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def num(n):
    if n > 0:
        return 'Positivo'
    else:
        return 'Negativo.'

n = int(input('Número: '))
print(num(n))