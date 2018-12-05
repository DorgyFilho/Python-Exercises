#005 - O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
#Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de 
#itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas 
#contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver 
#o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo
#abaixo:

# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

preco = 1.99

vQtd = False
while vQtd == False:
    qtd = input('Digite uma quantidade de 1 até 50: ')
    try:
        qtd = int(qtd)
        if not (0 < qtd <= 50):
            print('Digite apenas um valor entre 1 e 50. Tente novamente.')
        else:
            vQtd = True
    except:
        print('Digite apenas um valor inteiro. Tente novamente.')

print('\n')
print('{:50}'.format('TABELA DE PREÇOS - LOJA DE ARTIGOS'))
print('='*50)
for i in range(1, qtd+1):
    valor = preco*i
    print('{} - R${:.2f}'.format(i, valor))