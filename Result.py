phy = int(input("Enter Physics marks : "))
chem = int(input("Enter Chemistry marks : "))
bio = int(input("Enter Biology marks : "))
math = int(input("Enter Mathematics marks : "))
cmp = int(input("Enter Computer marks : "))
percentage= (phy+chem+bio+math+cmp)/5
print("Percentage is : ",percentage)
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
elif percentage>=40:
    print("Grade E")
else:
    print("Grade F")