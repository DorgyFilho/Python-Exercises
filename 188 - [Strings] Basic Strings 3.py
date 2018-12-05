def unusual(first, second):
    third = ''

    for letter in first:
        if letter not in second and letter not in third:
            third += letter

    for letter in second:
        if letter not in first and letter not in third:
            third += letter

    if third == '':
        print('Unusual characters not found.')
    else:
        print('Unusual characters: 'f"{third}")

first = input('First String: ').upper()
second = input('Second String: ').upper()
unusual(first, second)