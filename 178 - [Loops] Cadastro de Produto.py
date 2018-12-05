#178 - Exercício 5.15: Nilo Menezes

total = 0
price = 0
repeat = 'Y'
while repeat == 'Y':
    cod = int(input('Code: '))
    if cod == 0:
        break
    elif cod == 1:
        price += 0.50
    elif cod == 2:
        price += 1.00
    elif cod == 3:
        price += 2.00
    else:
        print('Invalid Option!')
    if price != 0:
        qtd = int(input('Number of Products: '))
        total += (qtd*price)
        print('Total: ${:.2f}'.format(total))

    print('Do you want to try again? Y or N\nChoose Your Option')
    repeat = input('Choose: ').upper()
    if repeat == 'N':
        break