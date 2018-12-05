#145 - Write a Python program to get the difference between the two lists.

lista1 = ['Dorgival', 'Cecilia', 'Shiro', 'Kauane']
lista2 = ['Cecilia', 'Kauane', 'John', 'Juliana']
dif = set(lista1).difference(set(lista2))
print(dif)