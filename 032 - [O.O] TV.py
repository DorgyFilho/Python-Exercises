#032 - Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
#O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
#Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:

    def __init__(self, canal='1', volume='0'):
        self.__canal = canal
        self.__volume = volume
    
    def canal(self):
        return self.__canal
    
    def selCan(self, num):
        if num.isdigit():
            can = int(input('Digite um número de 1 a 50: '))
            if 1 <= can <= 50:
                self.__canal = can
            else:
                print('Digite apenas um valor de 1 até 50. Tente novamente.')
        else:
            print('Só é válido digitar número inteiro.')
    
    def selVol(self, num):
        if num.isdigit():
            vol = int(input('Digite o nível de volume entre 1 e 40: '))
            if 0 <= vol <= 40:
                self.__volume = vol
            else:
                print('Volume máximo permitido: 40')
        else:
            print('Só é válido digitar número inteiro.')
    
    def mudaCan(self):
        can = input('Selecione um canal de 1 a 50: ')
        self.__canal = can
    
    def mudaVol(self):
        vol = input('Digite o nivel de volume entre 0 e 40: ')
        self.__volume = vol

    def __repr__(self):
        return 'Status\nCanal:{}\nVolume:{}'.format(self.__canal, self.__volume)

def main():
    tv = TV()
    while True:
        print(tv)
        print('{:50}'.format('SISTEMA DE TV'))
        print('='*50)
        print('Escolha uma opção\n1-Mudar Canal\n2-Mudar Volume\n3-Desligar')
        opcao = input('Escolha a opção desejada: ')
        if opcao == '1':
            tv.mudaCan()
        elif opcao == '2':
            tv.mudaVol()
        elif opcao == '3':
            print('Sistema de TV desligado.')
            break
        else:
            print('Erro! Opção inválida.')
            break

main()
            