#168 - Exercício 10.02 - Nilo Menezes: Página 220

class TV:
    def __init__(self, can, cmin, cmax):
        self.can = can
        self.cmin = cmin
        self.cmax = cmax
    
    def mudaBaixo(self):
        if self.can-1 >= self.cmin:
            self.can -= 1

    def mudaCima(self):
        if self.can-1 <= self.cmax:
            self.can += 1

    def mudaPrimeiro(self):
        if self.can > self.cmax:
            self.can = self.cmin
            return self.can
    
    def mudaUltimo(self):
        if self.can < self.cmin:
            self.can = self.cmax
            return self.can

cmin = int(input('Limite Mínimo: '))
cmax = int(input('Limite Máximo: '))
can = int(input('Canal Inicial: '))
tv = TV(can, cmin, cmax)
tv.mudaCima()
print(tv.can)
tv.mudaBaixo()
print(tv.can)
