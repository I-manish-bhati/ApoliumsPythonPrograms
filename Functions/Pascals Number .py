from math import factorial

def pas(x):
    for i in range(x+1):
        for j in range(x-i+1):
            print(" ",end="")
        for k in range(i+1):
            #nCr= n!//(n-r)!*r*
            print(factorial(i)//(factorial(i-k)*factorial(k)),end="  ")
        print()
        
    
x=int(input("Enter no. of terms : "))
pas(x)

