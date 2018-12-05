#138 - Write a Python program to get the last part of a string before a #specified character. 
#Ex: 'https://www.w3resource.com/python-exercises/string'

def exp(s):
    modif = ''
    if '/' in s:
        modif = s.rsplit('/', 1)[0]
        return modif

def exp2(s):
    modif2 = ''
    if '-' in s:
        modif2 = s.rsplit('-',1)[0]
        return modif2

s = input('Expressão: ')
print(exp(s))
print(exp2(s))


