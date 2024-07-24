l1=[2,3,5,6,3,7,3,2,9]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)