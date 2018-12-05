#095 - Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.

def misturar(p1, p2):
    str1 = p1[:2] + p2[2:]
    str2 = p2[:2] + p1[2:]

    return '{} ---> {}'.format(str1, str2)

str1 = input('Digite aqui: ')
str2 = input('Digite aqui: ')
print(misturar(str1,str2))