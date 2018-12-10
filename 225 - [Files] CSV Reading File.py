#229 - CSV Reading File

#Calculate the class average

#Read four notes and find the average.

#1 - Ordenation.
def selectSort(L):
    n = len(L)
    for i in range(n-1):
        maxi = i
        for j in range(i+1, n):
            if L[j] > L[maxi]:
                maxi = j
        L[i], L[maxi] = L[maxi], L[i]
    return L

#2 - Main Program
file1 = open(input('File: '), 'r')
L = []
qty = 0
for line in file1:
    lineList = line.split(',')
    average = (float(lineList[1])+float(lineList[2])+float(lineList[3])+float(lineList[4]))/4.0
    L.append(average)

ord = selectSort(L)
file1.close()
arq = open(input('New File: '), 'w')
for elem in ord:
    arq.write(str(elem))
    arq.write('\n')
arq.write('Average: {:.2f}'.format(sum(ord)/len(ord)))
arq.close()