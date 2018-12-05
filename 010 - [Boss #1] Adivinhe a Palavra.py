#010 - Desenvolva um jogo de adivinhar palavras. O programa terá uma lista de palavras lidas de um 
#arquivo-texto e escolherá uma aleatoriamente. 
#O jogador poderá errar 6 vezes antes de ser enforcado.

import random 

palavras = []
arq = open('/home/dorginho/sorteio.txt', 'r')
palavra = arq.readlines()
arq.close()

for i in palavra:
    palavras.append(i.strip())

pSorteada = random.choice(palavras)
pCerta = ''

erros = 0
while erros < 6:
    letra = input('Digite uma letra: ').upper()
    if letra in pSorteada:
        pCerta += letra

        sublinhados = 0
        for l in pSorteada:
            if l in pCerta:
                print(l, end=' ')
            else:
                print('_', end=' ')
                sublinhados += 1

        if sublinhados == 0 and erros == 0:
            print('Excepcional! Você acertou a palavra sem cometer erros!')
            break
        elif sublinhados == 0 and (1 <= erros < 6):
            print('Você acertou a palavra. Parabéns!')
            break
    else:
        erros += 1
        print('Você errou a {}° vez.'.format(erros))
else:
    print('Infelizmente você perdeu o jogo. A resposta certa é {}'.format(pSorteada))

