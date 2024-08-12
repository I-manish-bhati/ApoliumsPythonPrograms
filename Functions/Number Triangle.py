def pas(x):
    #print("hello")
    for i in range(1,x+1):
        print(" "*((x-i)*2),end="")
        for j in range(1,i):
            print(j,end=" ")
        for k in range(i,-1,-1):
            if k==0:
                pass
            else:
                
                print(k,end=" ")
        print("\n")

x=int(input("Enter the no of lines : "))
pas(x)