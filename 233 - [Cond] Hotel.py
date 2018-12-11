#237 - Hotel

name = input("What's Your Name?: ")
price = 60.00
daily = int(input('Hotel Rates: '))
if daily <  15:
    total = price + (daily*8.00)
    print(f'Total: ${total}')
elif daily > 15:
    total = price + (daily*5.50)
    print(f'Total: ${total}')
else:
    total = price + (daily*6.00)  

print(f'Name: {name}\nTotal: ${total}')

