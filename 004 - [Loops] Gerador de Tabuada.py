#004 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
#O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

a = int(input('Número a: '))
b = int(input('Número b: '))
if not (0 < b <= 10):
    print('Erro! Tabela não gerada.')
else:
    for i in range(1, b+1):
        res = a*i
        print('{} x {} = {}'.format(a,i,res))