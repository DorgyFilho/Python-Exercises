#136 - Write a Python program to remove the characters which have odd #index values of a given string.

def removePar(palavra):
    res = ''
    for i in range(len(palavra)):
        if i % 2 == 0:
            res += palavra[i]
    return res


palavra = input('Digite uma palavra: ')
print(removePar(palavra))
 
