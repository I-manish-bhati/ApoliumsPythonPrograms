x=int(input("Enter the no of stars : "))  
b=2
for i in range(1,x+1):
    print(" "*i,"* "*i," "*(x-i),"*","    "*(x-i),"*"," "*(x-i),"* "*i)

for i in range(0,x+1):
    if i<2:
        print(" "*(x-i),"* "*(x-i),"    "*i,"* "*b,"   "*i,"* "*(x-i))
        b-=1
    else:
        print(" "*(x-i),"* "*(x-i),"      "*i,"    ","* "*(x-i))
    
