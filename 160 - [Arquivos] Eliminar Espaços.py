#160 - Exercício 9.14 - Nilo Menezes: Página 194

import sys

if len(sys.argv) != 3:
    print('\nExercicio 160.py  entrada saida\n\n\n')
    sys.exit(1)

e = sys.argv[1]
s = sys.argv[2]

ent = open('/home/dorginho/exercicio.txt', 'r',encoding='utf-8')
sai = open('/home/dorginho/novo3.txt', 'w', encoding='utf-8')
branco = 0

for linha in ent.readlines():
    linha = linha.rstrip()
    linha = linha.strip()
    linha = linha.replace(' ', '')
    if linha == '':
        branco += 1
    else:
        branco = 0
    
    if branco < 2:
        sai.write(linha+'\n')


ent.close()
sai.close()