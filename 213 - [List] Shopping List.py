shopping = []
prod = ''
while prod != 'end':
    prod = input('Item: ')
    if prod == 'end':
        print('The End')
        break
    price = float(input('Price: '))
    shopping.append([prod, price])

print('Shopping List: 'f'{shopping}')
