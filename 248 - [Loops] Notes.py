#248 - Uma turma de inglês do curso “English Fast” tem 100
#alunos. Faça um algoritmo em python que leia a nota e o
#nome de cada um dos alunos. O algoritmo deve calcular a
#média de toda a turma e em seguida mostrar a média
#calculada e o nome do aluno que teve a maior nota.

student = 0
notes = 0
best = 0
winner = ''

while student < 3:
    name = input('Your Name: ')
    note = float(input('Your Note: '))
    student += 1
    notes += note

    if note > best:
        best = note
        winner = name


average = notes/student

print(f'Average: {average}')
print(f'Winner: {winner} / Note: {best}')
