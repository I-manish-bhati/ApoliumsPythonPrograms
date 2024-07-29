def myfunc(n,l1):
    x=input("Enter element : ")
    l1.append(x)
    n=n-1
    if n==0:
        print("List : ",l1)
    myfunc(n,l1)

l1=[]
n=int(input("Enter the no of elements you want to enter : "))
myfunc(n,l1)