l1=[1,2,3,4,5,6,7,8,9,10]
m1=l1[1]
m2=l1[1]
for i in range(len(l1)):
    if l1[i]>m1:
        m2=m1
        m1=l1[i]
print("Largest = ",m1)
print("Second largest = ",m2)