#135 - Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frente (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a parte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back 

def palavra(a, b):
    mA = int(len(a)/2)
    mB = int(len(b)/2)

    if not mA % 2 == 0:
        mA += 1
    if not mB % 2 == 0:
        mB += 1
    
    return a[:mA] + b[:mB] + a[mA:] + b[mB:]

a = input('1: ')
b = input('2: ')
print(palavra(a,b))

