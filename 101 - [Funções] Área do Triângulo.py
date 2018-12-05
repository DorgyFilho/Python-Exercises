#101 - Escreva uma função que receba a base e a altura de um triângulo e
#retorne sua área (A = (base x altura)/2).

def triangulo(b,h):
    area = (b * h)/2
    return 'A área do triângulo é {:.0f}'.format(area)

b = int(input('Base: '))
h = int(input('Altura: '))
resultado = triangulo(b,h)
print(resultado)
