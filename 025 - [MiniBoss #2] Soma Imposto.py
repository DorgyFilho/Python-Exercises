#025 - Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do
#imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def sImposto(tImp, custo):
    valor = tImp*custo
    novoValor = custo + valor
    return novoValor

custo = float(input('Digite o valor do custo: '))
taxa = float(input('Digite o valor da taxa: '))
tImp = taxa/100

total = sImposto(tImp, custo)
print('O novo valor é R${:.2f}'.format(total))
