import random
import string
import time

def generator(size=12, char=string.ascii_uppercase + ' '):
    List = []
    play = 'Y'
    while play == 'Y':
        sequence = ' '.join(random.choice(char) for _ in range(size))
        List.append(sequence)
        print('The End.')
        print()
        print('List: ' f'{List}')
        print()
        print('Do You Want to Try Again? Y or N')
        play = input('Choose Your Option: ').upper()
        if play == 'N':
            print('Turn Off')
            exit()
    else:
        print('Invalid Option.')

def main():
    again = 'Y'
    while again == 'Y':
        print('Key Generator\nSelect Your Option\nS-Start\nE-Exit')
        print()
        op = input('Answer: ').upper()
        if op == 'S':
            print(generator())
            print('Loading...')
            time.sleep(3)
        elif op == 'E':
            print('Turn Off.')
            exit()
        else:
            print('Invalid Answer')
        print()
        print('Do You Want to Try Again? Y or N')
        again = input('Answer: ').upper()
        if again == 'N':
            print('Shutdown!')
            exit()
    else:
        print('Invalid Answer.')

main()
