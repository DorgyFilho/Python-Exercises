#110 - Crie um programa que leia os arquivos pares.txt e ímpares.txt e que
# crie um só arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos,
# de forma a preservar a ordem numérica.

def lenum(arq):
    while True:
        num = arq.readline()
        if num == '':
            return None
        if num.strip != '':
            return int(num)

def escreverNum(arq, n):
    arq.write('{}'.format(n))

par = open(input('Par: '), 'r')
impar = open(input('Ímpar'), 'r')
saida = open('/home/dorginho/parImpar.txt', 'w')
nPar = lenum(par)
nImpar = lenum(impar)

while True:
    if nPar == None and nImpar == None:
        break
    elif nPar != None and (nImpar == None or nPar <= nImpar):
        escreverNum(saida, nPar)
        nPar = lenum(par)
    elif nImpar != None and (nPar == None or nImpar <= nPar):
        escreverNum(saida, nImpar)
        nImpar = lenum(impar)

par.close()
impar.close()
saida.close()

