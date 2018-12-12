def pValue(value, delay):
    if value < 0:
        return 'No value.'
    if delay > 0:
        tax = (3/100)*value
        extra = ((1/100)*delay)*value
        return value + tax + extra
    else:
        return value 

value = 1
while value != 0:
    value = float(input('Value: $ '))
    if value != 0:
        delay = int(input('Delay (Day): '))
        print(f'New Value: ${pValue(value,delay)}')
    else:
        print('Turn Off')
        exit()