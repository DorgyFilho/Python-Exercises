#179 - Exercício 5.22: Nilo Menezes

rep = 'Y'
while rep == 'Y':
    print('1-ADD\n2-MINUS\n3-MULTI\n4-DIV\n5-QUIT\nChoose Your Option')
    n = int(input('Choose: '))
    if n == 5:
        print('Turn Off')
        break
    if not n == 5:
        a = int(input('Any Number: '))
        b = int(input('Any Number 2: '))
        if n == 1:
            print('{} + {} = {}'.format(a,b,a+b))
        elif n == 2:
            print('{} - {} = {}'.format(a,b,a-b))
        elif n == 3:
            print('{} x {} = {}'.format(a,b,a*b))
        elif n == 4:
            print('{} / {} = {}'.format(a,b,a/b))
    else:
        print('Invalid Option!')
    
    print('Do you want to try again? Y or N\nChoose Your Option')
    rep = input('Option: ').upper()
    if rep == 'N':
        print('Turn Off')
        break