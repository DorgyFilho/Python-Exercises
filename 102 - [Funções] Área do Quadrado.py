#102 - Escreva uma função que receba o lado (l) de um quadrado e retorne
# sua área (A = lado2).

def quadrado(l):
    area = l*l
    return 'A área do quadrado é {:.0f}'.format(area)

l = int(input('Lado: '))
res = quadrado(l)
print(res)
