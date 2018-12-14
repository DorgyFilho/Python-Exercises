def RevHour(num):
    if num < 10:
        return '000' + str(num)
    elif num < 100:
        return '00' + str(num)
    elif num < 1000:
        return '0' + str(num)
    else:
        return str(num)

print('24h to 12h Converter')
num = int(input('Answer: '))
normal = 0
if num == 0000:
    normal = '12:00 A.M'
    print(normal)
elif num > 1200:
    normal = RevHour(num - 1200)
    print(normal[0:2] + ':' + normal[2:] + ' P.M')
else:
    normal = RevHour(num+1200)
    print(normal[0:2] + ':' + normal[2:] + ' A.M')

