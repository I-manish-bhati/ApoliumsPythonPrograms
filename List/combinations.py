t=(0,1,2,3,4,5,6)
l1=[]
l2=[]
l3=[]
for i in range(1000,6667):
    if i%10>6:
        pass
    else:
        l1.append(i)
print(len(l1))
for i in l1:
    if i%3==0:
        l2.append(i)
print(len(l2))