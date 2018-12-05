#088 - Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

lista = [1,2,3,4,5,6]
novaLista = []
for i, x in enumerate(lista):
    if i not in (0,4,5):
        novaLista.append(x)

print(novaLista)

