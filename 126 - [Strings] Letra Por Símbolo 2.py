#126 - Letra Por Símbolo 2. Agora substitua uma letra que se repete no início de uma palavra ou 
# frase por $.

def subs(frase):
    if letra in frase:
        velho = frase.split(letra, 1)
        novo = simb.join(velho)
        return novo
    else:
        return 'NULL'

frase = input('Digite uma frase ou uma palavra: ')
letra = input('Digite uma letra: ')
simb = '$'
print(subs(frase))