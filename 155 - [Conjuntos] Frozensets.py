#155 - Write a Python program to use of frozensets.

x = frozenset([1,2,3,4])
y = frozenset([3,4,5,6])
z = x.isdisjoint(y) #Verifica se há elementos comuns entre a e b. 
#Se registrar ocorrência, o resultado é False. Caso contrário, é True
print(z)
w = x.difference(y)
print(w)
k = x | y #União: Elementos de a e b unidos.
print(k)
a = x & y #Interseção
print(a)
b = x - y #Diferença
print(b)
c = x ^ y #Diferença Simétrica
print(c)