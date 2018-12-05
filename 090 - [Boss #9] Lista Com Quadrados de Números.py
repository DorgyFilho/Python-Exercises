#090 - Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30 (both included).


def numSqr():
    quadrado = list()
    for i in range(1,21):
        quadrado.append(i**2)
    print(quadrado[:5])
    print(quadrado[-5:])

numSqr()