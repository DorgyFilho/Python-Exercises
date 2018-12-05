#123 - Escreva uma função que recebe uma frase e uma palavra
# antiga e uma palavra nova. A função deve retornar uma
# string contendo a frase original, mas com a última
# ocorrência da palavra antiga substituída pela palavra nova. A
# entrada e saída de dados deve ser feita no programa
# principal. 

def substituir(frase):
    if nova not in frase: #Vou colocar você na frase
        resto = frase.rsplit(palavra, 1) #Elimina apenas a última incidência da palavra.
        novaFrase = nova.join(resto) #Nova frase construída.
        return novaFrase #Resultado.

#PROGRAMA PRINCIPAL
while True:
    frase = input('Digite uma frase: ').upper()
    palavra = input('Digite a palavra a ser substituída: ').upper()
    nova = input('Digite a nova palavra: ').upper()
    if palavra == 'FIM' and nova == 'FIM': #PROGRAMA ENCERRADO.
        print('Encerrado.')
        break
    else:
        print(substituir(frase)) #CHAMAR A FUNÇÃO

