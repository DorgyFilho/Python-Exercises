#165 - Exercício 8.7 - Nilo Menezes: Página 172

def mdc(a,b):
    if b == 0:
        return a 
    else:
        return mdc(b, a%b)

a = int(input('Número a: '))
b = int(input('Número b: '))
print('MDC de {} e {} é {}'.format(a, b, mdc(a,b)))