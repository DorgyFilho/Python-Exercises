#033 - Crie uma classe chamada Ingresso, que possui
# um valor em reais e um método imprimeValor()
# – Crie uma classe VIP, que herda de Ingresso e
# possui um valor adicional. Crie um método que
# retorne o valor do ingresso VIP (com o adicional
# incluído).

class Ingresso:
    atual = None

    def __init__(self, atual):
        self.atual = atual
    
    def impValor(self):
        return 'O valor do ingresso normal é R${:.2f}'.format(self.atual)
    
class VIP(Ingresso):
    valorVIP = None

    def __init__(self, valorVIP):
        Ingresso.__init__(self, valorVIP)
        self.valorVIP = valorVIP
    
    def ImpVip(self):
        return 'O valor do ingresso VIP é R${:.2f}'.format(self.valorVIP)

atual = float(input('Valor atual do ingresso: '))
add = float(input('Valor adicional: '))
novoValor = atual + add
Atual = Ingresso(atual)
print(Atual.impValor())
Vip = VIP(novoValor)
print(Vip.ImpVip())