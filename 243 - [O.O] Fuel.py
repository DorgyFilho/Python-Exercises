# #248 - Fuel

class Fuel:
    def __init__(self, stock, price):
        self.stock = stock
        self.price = price
    
    def addValue(self, value):
        Lts = value/self.price
        self.stock -= Lts
        return Lts
    
    def addLts(self, lts):
        Value = lts*self.price
        self.stock -= lts
        return Value
    
    def ChangePrice(self, newPrice):
        self.price = newPrice
    
    def ReloadFuel(self, lt):
        self.stock += lt

LITER = int(input('Liter: '))
PRICE = float(input('Price: '))
FUEL = Fuel(LITER, PRICE)
print(f'Added {FUEL.addValue(LITER)} liters')
print(f'Added ${FUEL.addLts(PRICE)}')
change = input('Do You Want to Change Price? Y or N: ').upper()
if change == 'Y':
    newPrice = float(input('New Price: '))
    FUEL.ChangePrice(newPrice)
    print(f'Added ${FUEL.addLts(LITER)}')
else:
    print(f'Added ${FUEL.addLts(LITER)}')
FUEL.ReloadFuel(LITER)
print(f'Capacity: {FUEL.stock} lts')


            
