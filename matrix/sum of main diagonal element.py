#program to calculate sum of main diagonal elements
l1=[[2,4,6],[8,10,12],[14,16,18]]
sum=0
for i in range(len(l1)):
    for j in range(len(l1[0])):
        if i==j:
            sum+=l1[i][j]
print("Sum = ",sum)