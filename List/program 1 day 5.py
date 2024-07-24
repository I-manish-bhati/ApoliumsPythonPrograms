l1=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        l1.append(i)
print("The list of numbers which are divisible by 7 and are multiples of 5 are :",l1)