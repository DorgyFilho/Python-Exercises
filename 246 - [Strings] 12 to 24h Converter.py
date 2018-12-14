HourMod = ''
def convHour(hour):
    if hour[-2:] == 'AM':
        if hour[:2] == '12':
            HourMod = str('00' + hour[2:8])
        else:
            HourMod = hour[:-2]
    elif hour[-2:] == 'PM':
        if hour[:2] == '12':
            HourMod = hour[:-2]
        else:
            HourMod = str(int(hour[:2]) + 12) + hour[2:8]
    return HourMod 
 

hour = input('Hour (HH:MM:SSAMorPM): ')
print(convHour(hour))