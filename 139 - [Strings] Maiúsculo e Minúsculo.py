 #139 - Write a Python script that takes input from the user and displays 
 #that input back in upper and lower cases.

def transform(frase, palavra):
    if palavra.isalpha():
        return frase + palavra.upper()

def transform2(frase, palavra):
    if palavra.isalpha():
        return frase + palavra.lower()

frase = 'Meu time favorito é '
palavra = input('Digite a palavra: ')
print(transform(frase, palavra))
print(transform2(frase, palavra))

