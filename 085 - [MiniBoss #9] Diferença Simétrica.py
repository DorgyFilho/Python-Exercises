#085 - Diferença Simétrica.

con1 = [1,2,3,4]
con2 = [3,4,5,6]
con = set(con1).symmetric_difference(con2)
conj = set(con2).symmetric_difference(con1)
print(con)
print(con2)