#008 - Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços 
#em branco), conte:

#a. quantos espaços em branco existem na frase.
#b. quantas vezes aparecem as vogais a, e, i, o, u.

frase = input('Digite uma frase: ')

letraA = frase.count('a')
letraE = frase.count('e')
letraI = frase.count('i')
letraO = frase.count('o')
letraU = frase.count('u')
espaco = frase.count(' ')

print('Letra A: {}'.format(letraA))
print('Letra E: {}'.format(letraE))
print('Letra I: {}'.format(letraI))
print('Letra O: {}'.format(letraO))
print('Letra U: {}'.format(letraU))
print('Espaços: {}'.format(espaco))