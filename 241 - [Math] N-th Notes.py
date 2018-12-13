#246 - Faça um programa que leia um número
#indeterminado de notas. Após esta entrada de
#dados, faça o seguinte:
#•Mostre a quantidade de notas que foram lidas.
#•Exiba todas as notas na ordem em que foram
#informadas.
#•Exiba todas as notas na ordem inversa à que
#foram informadas, uma abaixo do outra.
#•Calcule e mostre a soma das notas.
#•Calcule e mostre a média das notas.
#•Calcule e mostre a quantidade de notas acima
#da média calculada.

Notes = []
note = ''
while note != 0:
    note = float(input('Note: '))
    if note == 0:
        print('Turn Off!')
        break
    Notes.append(note)

scoreNotes = 0.0
for points in Notes:
    scoreNotes += points

avgNotes = scoreNotes/len(Notes)

maxAvg = 0
for superNotes in Notes:
    if superNotes > avgNotes:
        maxAvg += 1

Len = len(Notes)
InvNotes = Notes.reverse()

print(f'Reverse Notes: {Notes}')
Notes.reverse()
print(f'Original Notes: {Notes}')
print(f'Total of Inserted Notes: {Len}')
print(f'Total: {scoreNotes}')
print(f'Average: {avgNotes}')
print(f'Above Average: {maxAvg}')


