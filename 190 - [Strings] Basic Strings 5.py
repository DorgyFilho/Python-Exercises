def strings(str1, str2):
    str3 = ''
    for letra in str1:
        if letra not in str2:
            str3 += letra

    if str3 == '':
        print('All characters were removed.')
    else:
        print('Str 1: 'f'{str1}')
        print('Str 2: 'f'{str2}')
        print('Characters: 'f'{str3}')

str1 = input('String 1: ').upper()
str2 = input('String 2: ').upper()
strings(str1,str2)