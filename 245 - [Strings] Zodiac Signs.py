#Zodiac Signs.

def Zodiac():
    birthday = int(input('Your Birthday: '))
    if not (1 <= birthday <= 31):
        print('Invalid Answer!')
    month = input('Your Month: ').upper()
    if month == 'DECEMBER':
        result = 'Sagittarius' if birthday < 22 else 'Capricorn'
    elif month == 'JANUARY':
        result = 'Capricorn' if birthday < 21 else 'Aquarius'  
    elif month == 'FEBRAURY':
        result =  'Aquarius' if birthday < 18 else 'Pisces' 
    elif month == 'MARCH':
        result = 'Pisces' if birthday < 20 else 'Aries'
    elif month == 'APRIL':
        result = 'Aries' if birthday < 20 else 'Taurus'
    elif month == 'MAY':
        result = 'Taurus' if birthday < 21 else 'Gemini'
    elif month == 'JUNE':
        result = 'Gemini' if birthday < 21 else 'Cancer'
    elif month == 'JULY':
        result = 'Cancer' if birthday < 23 else 'Leo'
    elif month == 'AUGUST':
        result = 'Leo' if birthday < 23 else 'Virgo'
    elif month == 'SEPTEMBER':
        result = 'Virgo' if birthday < 23 else 'Libra'
    elif month == 'OCTOBER':
        result = 'Libra' if birthday < 22 else 'Scorpio'
    elif month == 'NOVEMBER':
        result = 'Scorpio' if birthday < 22 else 'Sagittarius'
    return f'Your Zodiac Sign: {result}'

def main():
    again = 'Y'
    while again == 'Y':
        print('Zodiac Signs\nChoose Your Option\n1-Start\n2-Quit')
        opt = input('Answer: ')
        if opt == '1':
            print(Zodiac())
        elif opt == '2':
            print('Turn Off')
            exit()
        else:
            print('Invalid Option!')
            break
        print()
        print('Do You Want to Try Again? Y or N')
        again = input('Option: ').upper()
        if again == 'N':
            print('Turn Off!')
            exit()
    else:
        print('Invalid Option!')

main()
