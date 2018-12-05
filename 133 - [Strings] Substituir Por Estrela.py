#133 - Dado uma string `s`, retornar uma string onde
# todas as ocorrências de seu primeiro caractere
# seja alterado para '*', exceto o primeiro caracter. Exemplo:
#
# babble ---> ba**le
#
# Presuma que o tamanho da string seja 1 ou mais.
# Dica: s.replace (strA, strB) retorna uma versão da string s.

def subst(s):
    frente = s[0]
    verso = s[1:]
    if frente in verso:
        novo = verso.rsplit(frente)
        novaS = '*'.join(novo)
        return frente + novaS
    else:
        return 'NULL'

s = input('Digite uma palavra: ')
print(subst(s))        
