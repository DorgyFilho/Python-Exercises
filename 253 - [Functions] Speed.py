#253 - Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”

def licDriver(speed):
    points = 0
    overspeed = ''
    excess = ''
    if speed <= 70:
        print('You are free.')
    elif speed > 70:
        overspeed = speed
        excess = overspeed - 70
        for number in range(1, excess+1):
            if number % 5 == 0:
                points += 1
        print(f'You Have {points} points')
        if points > 12:
            print('Your License Driver is Suspended')
    return ''


speed = int(input('Your Speed: '))
licDriver(speed)


