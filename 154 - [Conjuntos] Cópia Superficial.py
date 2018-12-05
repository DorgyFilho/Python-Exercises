#154 - Escreva um programa em Python para criar uma cópia superficial dos conjuntos.
#Nota: Cópia superficial é uma cópia bit-wise de um objeto. Um novo objeto é criado com 
#uma cópia exata dos valores no objeto original.

conA = set([1,2,3,4])
conB = set([5,6,7,8])
conC = conA.copy()
conD = conB.copy()
print(conC)
print(conD)
