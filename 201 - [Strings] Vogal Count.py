#201 - Elabore um programa que receba uma linha de texto e conte as vogais apresentando o respectivo
# histograma na seguinte forma:
# Exemplo:
# Linha de texto passada: “Na próxima quarta-feira é feriado.”
# a : ****** (6)
# e : *** (3)
# i : *** (3)
# o : ** (2)
# u : * (1)

phrase = input('Phrase: ')
a = phrase.count('a')
e = phrase.count('e')
i = phrase.count('i')
o = phrase.count('o')
u = phrase.count('u')

print('Letter a: ', end=' ')
print('*'*a)
print('Letter e: ', end=' ')
print('*'*e)
print('Letter i: ', end=' ')
print('*'*i)
print('Letter o: ', end=' ')
print('*'*o)
print('Letter u: ', end=' ')
print('*'*u)
