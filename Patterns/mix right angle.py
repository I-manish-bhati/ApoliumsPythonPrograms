x=int(input("Enter the no of stars : "))
for i in range(1,x+1):
    print("* "*i,"    "*(x-i),"* "*i)
print()
for i in range(0,x+1):
    print("* "*(x-i),"    "*i,"* "*(x-i))
    
for i in range(1,x+1):
    print(" "*(x-i),"* "*i)
    
