l1=[[11,12,13],[14,15,16],[17,18,19]]
l2=[[1,2,3],[4,5,6],[7,8,9]]
l3=[]
for i in range(len(l1)):
    x=[]
    for j in range(len(l1[i])):
        z=l1[i][j]+l2[i][j]
        x.append(z)
    l3.append(x)

print(l3)
"""for i in range(len(l3)):
    for j in range(len(l3[i])):
        print(l3[i][j],end="  ")
    print('\n')"""