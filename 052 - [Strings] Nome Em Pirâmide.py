#40 - Usando como base o código 40, imprima o nome em letra maiúscula e em formato de pirâmide.

#1 - Digite uma expressão.
nome = input('Digite um nome sem espaços: ').upper() #Quero o resultado em letra maiúscula.

#2 - Utilize a função len() para medir o tamanho da string.
tam = len(nome) #Será usada para calcular "espaco", que vem a seguir, dentro do for.

#3 - Utilize o for para percorrer a string.
for i in range(len(nome)): #Utilizei o len para que a string fosse percorrida.
    espaco = int((tam-i)/2) #Geradora de pirâmide.
    print(' '*espaco+nome[:i+1]) #Imprima a pirâmide.


