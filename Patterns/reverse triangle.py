x="* "
num=int(input("Enter the range : "))
for i in range(1,num+1):
    for k in range(i):
        print(" ",end="")
    print(num*x,end="")
    num=num-1
    print()
    


