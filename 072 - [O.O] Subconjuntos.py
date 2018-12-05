#072 - Write a Python program to get all possible unique subsets from a set of distinct integers.

class Conjunto:
    def subCon(self, sub):
        return self.geraSubConj([], sorted(sub))
    
    def geraSubConj(self, atual, sub):
        if sub: #Se for verdade...
            return self.geraSubConj(atual, sub[1:]) + self.geraSubConj(atual + [sub[0]], sub[1:])
        return [atual]

print(Conjunto().subCon([1,2,3]))