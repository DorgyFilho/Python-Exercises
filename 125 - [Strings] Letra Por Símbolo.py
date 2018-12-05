#125 - Write a Python program to get a string from a given string where all occurrences of its first char 
# have been changed to '$', except the first char itself. 

def subst(frase):
    if letra in frase:
        subs = frase.rsplit(letra, 1)
        novo = simb.join(subs)
        return novo
    else:
        return 'NULL'

frase = input('Digite uma frase: ')
letra = input('Digite uma letra: ')
simb = '$'
print(subst(frase))