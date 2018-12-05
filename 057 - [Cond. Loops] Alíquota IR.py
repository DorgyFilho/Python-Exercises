#057 - Entrar com o salário bruto de 10 pessoas. Imprimir nome e o valor da alíquota do imposto de
#renda.
#Salário < R$600,00 Isento
#Salário >= R$ 600,00 e < R$ 1.500,00 10% do salário bruto
#Salário >= R$1.500,00 15% do salário bruto
 
#1 - Crie o looping for e em seguida, informe seu nome e seu salário bruto.
for i in range(1,11):
    nome = input('Digite o seu nome: ')
    sBruto = float(input('Digite o seu salário bruto: '))
 
#2 - Estabeleça condições do IR e imprima o resultado.
    if sBruto < 600:
        print('{}, você é isento(s) de IR, pois recebe R${} de salário.'.format(nome, sBruto))
    elif sBruto >= 600 and sBruto < 1500:
        aliq = sBruto*(10/100)
        print('{}, você terá que pagar uma alíquota de R${} do IR.'.format(nome, aliq))
    elif sBruto >= 1500:
        aliq = sBruto*(15/100)
        print('{}, você terá que pagar uma alíquota de R${} do IR.'.format(nome, aliq))