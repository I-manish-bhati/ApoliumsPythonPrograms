x=int(input("Enter the amount you want to withdraw : "))
y=5000000
if x%5==0:
    y=y-x-0.5
    print("The amount after the transaction is ",y)
else:
    print("The transaction can't be initiated ")