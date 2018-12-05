#158 - Exercício 9.7 - Nilo Menezes: Página 194

L = 30
PG = 60
nomeArq = 'Exercício'

def verifica(arq, lin, pag):
    if lin == L:
        R = '{} - Página {}'.format(nomeArq, pag)
        arq.write(R.center(L-1)+'\n')
        pag += 1
        lin = 1
    return lin, pag

def escreve(arq, lin, Lin, pag):
    arq.write(lin+'\n')
    return verifica(arq, Lin+1, pag)

ent = open('/home/dorginho/exercicio.txt', 'r', encoding='utf-8')
sai = open('/home/dorginho/novo2.txt', 'w', encoding='utf-8')

pag = 1
linhas = 1

for linha in ent.readlines():
    palavras = linha.rstrip().split(' ')
    linha = ''
    for p in palavras:
        p = p.strip()
        if len(linha)+len(p)+1 > L:
            linhas, pag = escreve(sai, linha, linhas, pag)
            linha = ''
        linha += p+''
    if linha != '':
        linhas, pag = escreve(sai, linha, linhas, pag)

while linhas != 1:
    linhas, pag = escreve(sai, '', linhas, pag)

ent.close()
sai.close()
