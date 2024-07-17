x="*"
num=int(input("Enter the range : "))
for i in range(1,num+1):
    print(x*i)
    


for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    for k in range(1,2*i):
        print(x,end="")
    print()

print("\n")

for i in range(1,num+1):
    for j in range(0,i):
        print(" ",end="")
    for k in range(1,2*num-i):
        print(x,end="")
    print()