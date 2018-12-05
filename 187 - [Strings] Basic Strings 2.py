res = ''
str1 = input('Full String: ').upper()
str2 = input('Fragment String: ').upper()
if str2 in str1:
    res = str2
    print(f'{str2}')
else:
    print('Error!')