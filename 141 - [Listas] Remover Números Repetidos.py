#141 - Write a Python program to remove duplicates from a list.

lista = [1,2,2,3,3,4]
duplicados = []
for i in lista:
    if i not in duplicados:
        duplicados.append(i)

print(duplicados)