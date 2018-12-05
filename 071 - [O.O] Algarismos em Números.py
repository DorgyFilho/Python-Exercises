#071 - Faça um programa que converta algarismos em números.

class Alg2Num:

    def algNum(self, simb):
        alg = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for i in range(len(simb)):
            if i > 0 and (alg[simb[i]] > alg[simb[i-1]]):
                num += alg[simb[i]] - 2 * alg[simb[i-1]]
            else:
                num += alg[simb[i]]
        return num

ALG = input('Digite o número em algarismo: ').upper()
res = Alg2Num().algNum(ALG)
print('{} ---> {}'.format(ALG, res))