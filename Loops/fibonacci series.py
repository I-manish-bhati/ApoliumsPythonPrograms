r=int(input("Enter the no. of digits : "))
x,y=0,1
c=1
print("Fibonacci series : ",end=" ")
for i in range(1,r+1):
    print(x, end=" ")
    x=y
    y=c
    c=x+y