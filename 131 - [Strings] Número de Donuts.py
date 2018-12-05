#131 - Dado um `count` como sendo o números de donuts, retornar uma string
# na forma "Número de donuts: <count>", caso `count` seja
# maior ou igual a 10 retornar "many". 

def donuts(count):
    if count < 10:
        return 'Número de Donuts: {}'.format(count)
    else:
        return 'Número de Donuts: Many'

palavra = input('Informe uma palavra: ')
count = len(palavra)
print(donuts(count))

