def Plates(op):
    plate = 10
    plates = list(range(1, plate+1))
    while True:
        print('There are {} plates.'.format(plate))
        print()
        print('Choose Your Option:\nA-Add\nR-Remove\nE-Exit')
        print()
        op = input('Choose: ').upper()
        if op == 'A':
            plate += 1
            plates.append(plate)
            print('Status:{}'.format(plates))
            print(f"{plates}")
        elif op == 'R':
            if len(plates) > 0:
                plate -= 1
                rm = plates.pop(-1)
                print('{} plates left.'.format(plate))
                print('Status: {}'.format(plates))
            else:
                print('Empty!')
        elif op == 'E':
            print('End of Game')
            break
    else:
        print('Invalid Option! Choose A, R or E')
    
op = ''
Plates(op)
