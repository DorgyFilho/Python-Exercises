#233 - Reversed Date

def RevDate(Date):
    splitDate = Date.split('/')
    InvDate = splitDate[::-1]
    return "/".join(InvDate)

Date = input('Date DD/MM/AAAA: ')
print(RevDate(Date))