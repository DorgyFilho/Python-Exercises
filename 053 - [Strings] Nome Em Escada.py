#053 - Usando como base o código 38, imprima o nome em letra maiúscula e em formato de escada.

#1 - Digite um nome em letra maiúscula.
nome = input('Digite seu nome: ').upper() #Quero o resultado em letra maiúscula.

#2 - Utilize a função len() para medir o tamanho da string.
tam = len(nome) #Usar para calcular a divisão na variável 'espaco', que virá em seguida.

#3 - Crie um looping for que leia o comprimento da string.
for i in range(len(nome)): #Lerá o comprimento da string.
    espaco = int((tam-i)/2) #Transformei em inteiro para que, no momento de gerar a string, o formato seja de escada
    print(""*espaco+nome[:i+1])#Concatenando...
