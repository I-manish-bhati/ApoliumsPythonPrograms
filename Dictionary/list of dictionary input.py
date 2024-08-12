ml=[{},{},{}]

for j in range(len(ml)):
    x={}
    print("Enter no of keys in iteration ",j+1," : ",end="")
    i=int(input(""))
    for i in range(i):
        if i==3:
            k=input("Enter key : ")
            l=int(input("Enter the length of array : "))
            v=[]
            for m in range(l):
                v.append(input("Enter the value : "))
        else:
            k=input("Enter key : ")
            v=input("Enter Value : ")
        x[k]=v
    ml[j]=x
print(ml)
