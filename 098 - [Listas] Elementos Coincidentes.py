#098 - Write a Python function that takes two lists and returns True if they have at least one common member

def achei(lista1, lista2):
    for elem in lista1:
        if elem in lista2:
            return True
        else:
            return False
    return 'Programa Encerrado.'

lista1 = list(range(1,10,2))
lista2 = list(range(1,10))
print(achei(lista1,lista2))