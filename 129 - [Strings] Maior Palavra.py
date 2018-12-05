 #129 - Write a Python function that takes a list of words and returns the length of the longest one

def maior(palavra):
    tamPalavras = []
    for i in palavra:
        tamPalavras.append((len(i), i))
    tamPalavras.sort()
    return tamPalavras[-1][1]

palavra = []
for i in range(1,4):
    palavras = input('{}° palavra: '.format(i)).upper()
    palavra.append(palavras)

print(maior(palavra))