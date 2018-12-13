#247 - Crie um programa que leia um arquivo e informe a última palavra existente.

files = open(input('File: '), 'r')
Names = files.readlines()
files.close()

for last in range(len(Names)):
    Last = Names[-1]
print(Last)