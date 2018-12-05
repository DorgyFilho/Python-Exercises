#094 - Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.

def addString(palavra):
    tam = len(palavra)
    if tam > 2:
        if palavra[-3:] == 'ING':
            palavra += 'LY'
        else:
            palavra += 'ING'
    
    return palavra

palavra = input('Digite uma palavra: ').upper()
resultado = addString(palavra)
print('{} ---> {}'.format(palavra, resultado))