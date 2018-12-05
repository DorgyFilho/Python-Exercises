#130 - Write a Python program to remove the nth index character from a nonempty string

def remover(palavra, n): 
    p1 = palavra[:n]     #n é o valor argumentativo que determinará a posição a ser removida.
    p2 = palavra[n+1:]   #A remoção só será válida se, e somente se, a posição estiver ao alcance do 
                         #tamanho da palavra digitada
    return p1+p2

palavra = input('Digite a palavra: ') #Digite a palavra.
tam = len(palavra) #Medir o tamanho da palavra.
pos = int(input('Posição a ser removida: ')) #Posição a ser removida.
if pos > tam: #Não pode!!!
    print('Posição maior que o tamanho da palavra.')
else: #Posição dentro dos limites do tamanho da string.
    print(remover(palavra, pos))