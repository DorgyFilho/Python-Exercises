#074 - Write a Python class named Circle constructed by a radius 
#and two methods which will compute the area and the perimeter of a circle.

class Circulo:

    def __init__(self, r):
        self.raio = r
    
    def Area(self):
        return (self.raio ** 2) * 3.14
    
    def Perimetro(self):
        return 2*self.raio*3.14

cir = int(input('Círculo: '))
Novo = Circulo(cir)
AREA = Novo.Area()
PERIMETRO = Novo.Perimetro()
print('Área: {}'.format(AREA))
print('Perimetro: {}'.format(PERIMETRO))