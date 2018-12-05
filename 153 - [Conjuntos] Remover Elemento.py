#153 - Write a Python program to remove an item from a set if it is present in the set.

A = set([1,2,3,4,5])
elem = int(input('Digite o elemento a ser removido: '))
if elem in A:
    A.discard(elem)
    print(A)
else:
    print('Elemento não existe.')