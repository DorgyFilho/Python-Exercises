#177 - Exercício 5.3: Nilo Menezes

import time

cont = 11
while cont > 0:
    cont -= 1
    time.sleep(1)
    print(cont)
    if cont == 0:
        time.sleep(1)
        print('Boom!')