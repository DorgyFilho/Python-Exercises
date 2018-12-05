#157 - Exercício 9.2 - Nilo Menezes: Página 192

import sys

if len(sys.argv) != 4:
    print('\nexercicio.py exercicio inicio fim\n\n')
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arq = open('/home/dorginho/exercicio.py', 'r')
    for linha in arq.readlines()[inicio-1:fim]:
        print(linha[:-1])

    arq.close()