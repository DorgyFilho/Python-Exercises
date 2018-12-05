#086 - Remover duplicados de uma lista.

lista = [1,2,2,3,4,4,5,6,7,8,8,9]
duplic = set()
unicos = []

for x in lista:
    if x not in duplic:
        unicos.append(x)
        duplic.add(x)

print(duplic)


