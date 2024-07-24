n=int(input("Enter the length of the track : "))
k=int(input("Enter the best speed stretch(in meters) : "))
n=n*1000
girls=(2,4,8,1,2,1,8)
gap=int(n//len(girls))
print(len(girls))
z=int(k//gap)
print("Z",z)
m=0
a,sum=0,0
for j in range(a,z):
    sum+=girls[j]
for i in range(z,len(girls)):
    if sum>m:
        m=sum
    sum=sum-girls[a]+girls[z]
    a+=1
print(m)
    