#036 - O.O: Retângulo. Calcule a área e o perímetro.

class Retangulo:

    ladoA = None
    ladoB = None

    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def calArea(self):
        return ladoA*ladoB
    
    def calPer(self):
        return 2*ladoA + 2*ladoB

ladoA = int(input('Lado A: '))
ladoB = int(input('Lado B: '))
obj = Retangulo(ladoA, ladoB)
print('A área é {}'.format(obj.calArea()))
print('O Perímetro é {}'.format(obj.calPer()))