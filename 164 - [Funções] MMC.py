#164 - Exercício 8.8 - Nilo Menezes: Página 172

def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)

def mmc(a,b):
    return abs(a*b) / mdc(a,b)

a = int(input('Número a: '))
b = int(input('Número b: '))
print('O MMC de {} e {} é {:.0f}'.format(a, b, mmc(a,b)))