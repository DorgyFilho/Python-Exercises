#105 - Crie um programa que desenhe um retângulo.

def retangulo(l, a, c='*'):
    linha = c * l
    for i in range(a):
        print(linha)
    return ''

l = int(input('Largura: '))
a = int(input('Altura: '))
res = retangulo(l,a)
print(res)