def plus(a,b):
    Plus = a + b
    return 'Result: ' f'{Plus}' 
def minus(a,b):
    Minus = a - b
    return 'Result: ' f'{Minus}'
def multi(a,b):
    Multi = a * b
    return 'Result: ' f'{Multi}'
def div(a,b):
    Div = a/b
    return 'Result: ' f'{Div}'

def main():
    again = 'Y'
    while again == 'Y':
        a = int(input('Number a: '))
        b = int(input('Number b: '))
        print('Choose Your Option\n1-Plus\n2-Minus\n3-Multi\n4-Div\n0-Exit')
        op = input('Option: ')
        if op == '0':
            print('I Quit.')
        elif op == '1':
            print(plus(a,b))
        elif op == '2':
            print(minus(a,b))
        elif op == '3':
            print(multi(a,b))
        elif op == '4':
            print(div(a,b))
        else:
            print('Invalid Option.')
    
        print('Do you want to try again? Y or N')
        print('Choose Your Option')
        again = input('Option: ').upper()
        if again == 'N':
            print('Turn Off')
        else:
            print('Invalid Option.')

main()