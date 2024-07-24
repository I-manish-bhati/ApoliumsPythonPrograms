l1=[1,2,3,3,3,1,2,2]
l2=[]
for i in l1:
    count=0
    for j in range(len(l1)):
        if i==l1[j]:
            count+=1
    if i not in l2 and count%2!=0:
        l2.append(i)
print("The list of dalls with missing pairs : ",l2)
