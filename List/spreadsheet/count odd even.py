l1=[1,2,3,4,5,6,7,8,9,10]
c1,c2=0,0
for i in l1:
    if i%2==0:
        c1=c1+1
    else:
        c2=c2+1
print("Even = ",c1," and Odd = ",c2)