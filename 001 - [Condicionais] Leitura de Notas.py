#001 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um 
#semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0        A
# Entre 7.5 e 9.0         B
# Entre 6.0 e 7.5         C
# Entre 4.0 e 6.0         D
# Entre 4.0 e zero        E

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1+n2)/2

if 9.0 < media <= 10:
  res = 'Conceito A'
elif 7.5 < media <= 9.0:
  res = 'Conceito B'
elif 6.0 < media <= 7.5:
  res = 'Conceito C'
elif 4.0 < media <= 6.0:
  res = 'Conceito D'
elif 0.0 <= media <= 4.0:
  res = 'Conceito E'

print('{:50}'.format('RESULTADO'))
print('='*50)
print('Nota 1: {}'.format(n1))
print('Nota 2: {}'.format(n2))
print('Média: {}'.format(media))
print('Resultado: {}'.format(res))