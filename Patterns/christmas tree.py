s=int(input("Enter no. of stars : "))
l=int(input("Enter the size of tree : "))
for i in range(1,s+1):
    print(" "*(s-i),"* "*i)
for i in range(l):
    for j in range(3):
        print(" "*(3-j),end="")
        if j==0:
            print("* "*(s-2))
        elif j==1:
            print("* "*(s-1))
        else:
            print("* "*s)
for i in range(3):
    print("  "*(s//2),end="* *")
    print()
print("*"*(s*2))