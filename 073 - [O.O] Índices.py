#073 - Write a Python program to find a pair of elements (indices of the two numbers) from a given 
#array whose sum equals a specific target number.

class Indice:
    def soma(self, nums, alvo):
        dicNum = {}
        for i, num in enumerate(nums):
            if alvo - num in dicNum:
                return (dicNum[alvo-num] + 1, i+1)
            dicNum[num] = i
print('Índice 1: %d, Índice 2: %d' % Indice().soma((10,20,10,40,50,60,70),50))