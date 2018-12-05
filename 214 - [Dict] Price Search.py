def search():
    prod = {'tomato': 1.50, 'beans': 1.25, 'water': 1.00, 'coffee': 1.00}
    msg = 'Item or "end" to turn off: '
    while True:
        item = input(msg).lower()
        if item == 'end':
            print('Turn off')
            break
        if item in prod:
            print('Price: $'f'{prod[item]}')
        else:
            print('Item not found')

search()