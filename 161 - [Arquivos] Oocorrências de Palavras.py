#161 - Exercício 9.11 - Nilo Menezes: Página 195

import sys

if len(sys.argv) != 2:
    print('\nExercicio: 161.py arquivo1\n\n\n')
    sys.exit(1)

nome = sys.argv[1]
dic = {}

arq = open(nome, 'r', encoding='utf-8')
for lin in arq:
    lin = lin.strip().lower()
    palavras = lin.split()
    for p in palavras:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1

arq.close()

for chave in dic:
    print('{} = {}'.format(chave, dic[chave]))          
