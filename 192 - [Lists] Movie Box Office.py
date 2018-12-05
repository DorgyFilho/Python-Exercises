seating = [10,2,25,17,0] #Available vacancies in each movie theater
while True:
    mTheater = int(input('Choose your movie theater or 0 to quit: ')) #List position.
    if mTheater == 0:
        print('I quit')
        break
    if mTheater > len(seating) or mTheater < 1:
        print('Invalid movie theater.')
    elif seating[mTheater-1] == 0:
        print('All seats are occupied.')
    else:
        print('How many places do you want to buy? Available: 'f'{seating[mTheater-1]}')
        armChair = int(input('Choose: '))
        if armChair > seating[mTheater-1]:
            print('Not available')
        elif armChair < 0:
            print('Invalid number')
        else:
            seating[mTheater-1] -= armChair
            print('Sold armChairs: 'f'{armChair}')

print('Rooms')
for i, j in enumerate(seating):
    print('Room: 'f'{i}')
    print('Empty Armchairs: 'f'{j}')

