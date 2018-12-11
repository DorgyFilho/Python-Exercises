#234 - Cash Machine
# money = int(input('Amount to be withdrawn: '))
# print(f'Total of ${maxBallot} dollar bills is {ballot}.')
#print('Welcome to the Dorgy Bank')
#print('Choose Your Option\n1-cashOut\n2-Exit)

def cashOut():
    money = int(input('Amount to be withdrawn: '))
    total = money
    maxBill = 100
    bill = 0

    while True:
        if total >= maxBill:
            total -= maxBill
            bill += 1
        else:
            if bill > 0:
                print(f'Total of ${maxBill} dollar bills is {bill}.')
            if maxBill == 100:
                maxBill = 50
            elif maxBill == 50:
                maxBill = 20
            elif maxBill == 20:
                maxBill = 10
            elif maxBill == 10:
                maxBill = 5
            elif maxBill == 5:
                maxBill = 2
            elif maxBill == 2:
                maxBill = 1
            bill = 0
            if total == 0:
                break
        
def main():
    again = 'Y'
    while again == 'Y':
        print()
        print('Welcome to the Dorgy Bank\nChoose Your Option\n1-Cash Out\n2-Exit')
        print()
        opt = input('Answer: ')
        if opt == '1':
            cashOut()
        elif opt == '2':
            print('Leaving the Bank...')
        else:
            print('Invalid Option!')
        print()
        print('Do You Want to Try Again? Y or N')
        again = input('Option: ').upper()
        if again == 'N':
            print('Turn Off')
            print('Thank you and always come back to Dorgy Bank')
            exit()
    else:
        print('Invalid Option')

main()
