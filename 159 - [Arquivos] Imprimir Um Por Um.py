#159 - Exercício 9.9 - Nilo Menezes: Página 194

import sys

if len(sys.argv) < 2:
    print('\nExercicio: 159.py [arquivo1 arquivo2 arquivoN]\n\n\n')
    sys.exit(1)

for nome in sys.argv[1:]:
    arquivo = open('/home/dorginho/exercicio.py', 'r')
    for linha in arquivo:
        print(linha, end=' ')

    arquivo.close()
