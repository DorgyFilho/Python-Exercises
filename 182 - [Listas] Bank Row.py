#182 - Bank Row

def row():
    last = 10
    row = list(range(1,last+1))
    while True:
        print('There are {} clients in a row.'.format(last))
        op = input('Choose Your Option: ').upper()
        if op not in ['A', 'R', 'Q']:
            print('Error! Invalid Option.')
        if op == 'A':
            last += 1
            row.append(last)
            print(row)
        elif op == 'R':
            if last > 0:
                last -= 1
                exitClient = row.pop(0)
                print(row)
                if last == 0:
                    print('End of Work.')
                    print(row)
        elif op == 'Q':
            print('Turn Off.')
            break

row()   
