#048 - Altere o programa 98, intercalando 3 vetores de 10 elementos cada.
 
#1 - Crie quatro listas, sendo l1, l2 e l3 com 10 elementos cada, enquanto l4 é vazia.
l1 = [1,3,5,7,9,11,13,15,17,19]
l2 = [2,4,6,8,10,12,14,16,18,20]
l3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
l4 = []
 
#2 - Crie um looping for e utilize a função zip para intercalar as listas.
for i,j,k in zip(l1,l2,l3):
    l4.append(i) #lista 1
    l4.append(j) #lista 2
    l4.append(k) #lista 3
 
 
#3 - Imprima o resultado.
print(l1)
print(l2)
print(l3)
print(l4)