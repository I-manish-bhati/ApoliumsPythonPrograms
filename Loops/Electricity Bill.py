units = int(input("Enter the units : "))
bill = 0
u=0
for i in range(1,51):
    if u== units:
        break
    bill = bill + 0.50
    u+=1
for i in range(51,151):
    if u==units:
        break
    bill = bill + 0.75
    u+=1
for i in range(151,251):
    if u==units:
        break
    bill = bill + 1.20
    u+=1
while u>250:
    if u== units:
        break
    bill = bill + 1.50
    u=u+1
extra = bill + bill*20/100
print("Your bill = ",extra)