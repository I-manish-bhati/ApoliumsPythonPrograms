l1=[2,3,4,6,5,5,3,2,8,8,8,5,6]
l2=[]
for i in range(len(l1)):
    count=0
    for k in range(len(l2)):
        if l2[k]==l1[i]:
            break
    else:
        for j in range(i,len(l1)):
            if l1[i]==l1[j]:
                count+=1
                l2.append(l1[i])
        if count>=2:
            print("List contains ",count-1,"duplicates of ",l1[i])
    
