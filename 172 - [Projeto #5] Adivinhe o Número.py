#172 - Adivinhe o Número.

import random

for i in range(1):
    sorteado = random.randint(0,100)

tent = 5
while tent > 0:
    tent -= 1
    num = int(input('Digite o número: '))
    if num > sorteado:
        print('O número é maior que o sorteado.\nVocê tem {} chance(s)'.format(tent))
    elif num < sorteado:
        print('O número é menor que o sorteado.\nVocê tem {} chance(s)'.format(tent))
    elif num == sorteado:
        print('Você acertou!')
        break
    if tent == 0:
        print('O jogo acabou. Infelizmente você perdeu.\nResposta certa: {}'.format(sorteado))
        break


    
