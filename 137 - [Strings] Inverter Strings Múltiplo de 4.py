#137 - Write a Python function to reverse a string if it's length is a #multiple of 4. 

def revStr(palavra):
    pInv = ''
    if tam % 4 == 0:
        pInv = palavra[::-1]
        return pInv
    else:
        return palavra

palavra = input('Digite uma palavra: ')
tam = len(palavra)
print(revStr(palavra))