#080 - Write a Python program to count the number of even and odd numbers from a series of numbers.

numeros = (1,2,3,4,5,6,7,8,9,0)
pares = 0
impares = 0
for i in numeros:
    if i%2 == 0:
        pares += 1
    else:
        impares += 1

print('Pares: {}'.format(pares))
print('Ímpares: {}'.format(impares))