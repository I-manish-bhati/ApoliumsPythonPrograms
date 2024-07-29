import cmath
a=float(input("Enter a : "))
b=float(input("Enter b : "))
c=float(input("Enter c : "))

#x=(-b+-sqrt(b2-4ac))
eq1=cmath.sqrt(((b**2)-(4*a*c))*0.5)
sol1=(-b+eq1)/2*a
sol2=(-b-eq1)/2*a
print("sol1 : ",sol1," Sol2 : ",sol2)