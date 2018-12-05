#015 - Escreva um programa que intercale os elementos de duas listas l1 e l2. Exemplo:
#para l1 = [1,2,4,8,16] e l2 =['a','b','c','d','e'], o programa deve computar a lista
#[1,'a',2,'b',3,'c','d','e']

l1 = [1,2,4,8,16]
l2 = ['a', 'b', 'c', 'd', 'e']
l3 = []

for i, j in zip(l1,l2):
    l3.append(i)
    l3.append(j)

print(l3)
