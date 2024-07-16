side1= int(input("Enter side 1 = "))
side2=int(input("Enter side 2 = "))
side3=int(input("Enter side 3 = "))
if side1==side2==side3:
    print("Equilateral Triangle")
elif side1!=side2!=side3:
    print("Scalene Triangle")
else:
    print("Isoceles Triangle")