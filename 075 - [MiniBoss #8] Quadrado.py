#075 - Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Retornar valor do Lado e calcular Área.

class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mostraLado(self):
        return self.lado

    def Area(self):
        area = self.lado*self.lado
        return 'A área é {}'.format(area)

lado = int(input('Lado: '))
res = Quadrado(lado)
print(res.mostraLado())
print(res.Area())