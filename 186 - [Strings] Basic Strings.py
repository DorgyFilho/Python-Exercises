def string(str1,str2):
    str3 = ''
    if str2 in str1:
        str3 = str2
        print(f'{str3}')
    else:
        print('Error!')

str1 = input('Full String: ').upper()
str2 = input('Search a str1 fragment: ').upper()
string(str1, str2)
    