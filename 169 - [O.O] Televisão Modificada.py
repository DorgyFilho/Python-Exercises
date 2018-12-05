#169 - Exercício 10.03 - Nilo Menezes: Página 221

class TV:
    def __init__(self, can, cmin, cmax):
        self.can = can
        self.cmin = cmin
        self.cmax = cmax
    
    def mudaBaixo(self):
        if self.can-1 >= self.cmin:
            self.can -= 1
        else:
            self.can = self.cmax
    
    def mudaCima(self):
        if self.can+1 <= self.cmax:
            self.can += 1
        else:
            self.can = self.cmin

can = int(input('Canal: '))
cmin = int(input('Mínimo: '))
cmax = int(input('Máximo: '))
tv = TV(can, cmin, cmax)
tv.mudaCima()
print(tv.can)