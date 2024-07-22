x="* "
num= int(input("Enter the range : "))
for i in range(1,num+1):
    for j in range(num):
        print(" "*num,end="")
    for k in range(i):
        print(x,end="")
    num=num-1
    print("\n")