#121 - TV

class TV:

    def __init__(self, can='1', vol='0'):
        self.__can = can
        self.__vol = vol
    
    def canal(self):
        return self.__can

    def escCan(self, num):
        if num.isdigit():
            can = int(input('Digite um canal de 1 a 100: '))
            if 1 <= can <= 100:
                self.__can = can
            else:
                print('Digite apenas um canal de 1 a 100.')
        else:
            print('Digite apenas valor numérico.')
    
    def escVol(self, num):
        if num.isdigit():
            vol = int(input('Digite o nível de volume entre 0 e 40: '))
            if 0 <= vol <= 40:
                self.__vol = vol
            else:
                print('Volume máximo permitido: 40.')
        else:
            print('Digite apenas valor numérico.')
    
    def mudaCan(self):
        can = input('Digite um canal de 1 a 100: ')
        self.__can = can

    def mudaVol(self):
        vol = input('Digite o nível de volume de 0 a 40: ')
        self.__vol = vol
    
    def __repr__(self):
        return 'NETWORK TV\nCANAL:{}\nVOLUME:{}'.format(self.__can, self.__vol)

def main():
    tv = TV()
    while True:
        print(tv)
        print('BEM-VINDO(A) À NETWORK TV\nESCOLHA UMA DAS OPÇÕES ABAIXO\n1-Mudar Canal\n2-Mudar Volume\n3-Desligar')
        print('='*30)
        op = input('Digite aqui a opção desejada: ')
        if op == '1':
            tv.mudaCan()
        elif op == '2':
            tv.mudaVol()
        elif op == '3':
            print('Sistema Encerrado.')
            break
        else:
            print('Opção Inválida.')
            break

main()