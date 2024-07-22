units = int(input("Enter the units : "))
bill = 0
if units<=50:
    bill = units*0.5
elif units>0 and units<=150:
    bill = (50*0.75)+((units-50)*0.75)
elif units>150 and units<=250:
    bill = (50*0.5)+(100*0.75)+((units-150)*1.2)
else:
    bill = (50*0.5)+(100*0.75)+(100*1.2)+((units-250)*1.5)
extra = bill + bill*20/100
print("Your bill = ",extra)