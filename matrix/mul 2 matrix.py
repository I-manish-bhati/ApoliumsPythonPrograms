l1=[[1,2],[4,5]]
l2=[[11,12],[14,15]]
l3=[[0,0],[0,0]]
for i in range(len(l1)):
    
    for j in range(len(l2[0])):
        l3[i][j] = l1[i][j]*l2[j][i]+l1[i][j+1]*l1[j][i]
    print("\n",l3[i])

