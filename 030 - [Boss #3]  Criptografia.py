#030 - Crie um programa que faca criptografia de dados.
# Ele deve ler um arquivo texto e gerar um outro arquivo criptografado
# da seguinte forma: Z->P, R->O, N->L, O->Z, P->R, L->N onde a primeira
# deve ser substituida pela segunda. Depois crie um programa para descriptografar.

def cripto(ent, sai):
    dicTroca = {'Z':'P', 'R':'O','N':'L', 'O':'Z', 'P':'R', 'L':'N', 'z':'p', 'r':'o', 'n':'l',
    'o':'z', 'p':'r', 'l':'n'}

    entrada = open(ent)
    saida = open(sai, 'w')

    texto = entrada.read()
    entrada.close()

    for elem in texto:
        if elem in dicTroca.keys():
            saida.write(dicTroca[elem])
        else:
            saida.write(elem)
    
    saida.close()

def descripto(ent2, sai2):
    dicInv = {'P':'Z', 'O':'R','L':'N', 'Z':'O', 'R':'P', 'N':'L', 'p':'z', 'o':'r', 'l':'n',
    'z':'o', 'r':'p', 'n':'l'}

    entrada = open(ent2)
    saida = open(sai2, 'w')

    texto = entrada.read()
    entrada.close()

    for elem in texto:
        if elem in dicInv.keys():
            saida.write(dicInv[elem])
        else:
            saida.write(elem)
    
    saida.close()

ent = input('Entrada: ')
sai = input('Criptografar: ')
ent2 = input('Entrada: ')
sai2 = input('Descriptografar: ')

cripto(ent, sai)
descripto(ent2, sai2)