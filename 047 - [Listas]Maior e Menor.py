#047 - Ler um vetor com 20 idades e exibir a
#maior e menor.
 
#1 - Crie uma lista vazia denominada 'idades'.
idades = []
 
#2 - Crie um looping for para digitar as idades pedidas no enunciado.
for i in range(1, 4): #Percorre o período mencionado para digitar as idades.
    idade = int(input('Digite a %d° idade: '%i)) #Poder especial para mostrar a ordinalidade.
    idades.append(idade) #Armazenar na lista.
 
#3 - Descubra com os métodos max e min a maior e a menor idade da lista.
maior = max(idades)
menor = min(idades)
 
#4 - Imprima o resultado.
print('Maior idade: {} ----> Menor idade: {}'.format(maior, menor))