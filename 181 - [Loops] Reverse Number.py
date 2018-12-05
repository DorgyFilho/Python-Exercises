#181 - Exercício 5.27: Nilo Menezes

test = 'Y'
while test == 'Y':
    num = int(input('Number: '))
    strnum = str(num)
    strInv = strnum[::-1]
    if strnum == strInv:
        print('{} = {}'.format(strnum, strInv))
    else:
        print('Not Palindrome')
    print('Do you want to try again? Y or N\nChoose Your Option')
    test = input('Option: ').upper()
    if test == 'N':
        print('Turn Off.')
        break
else:
    print('Error!')

