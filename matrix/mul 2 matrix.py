l1=[[1,2],[4,5]]
l2=[[11,12],[14,15]]
l3=[[0,0],[0,0]]
for i in range(len(l1)):
    for j in range(len(l2[0])):
        for k in range(len(l2)):
            
            l3[i][j] += l1[i][k]*l2[k][j]
    print(l3[i])

