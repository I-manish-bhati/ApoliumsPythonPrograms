l1=[2,4,6,8,10,12,2,14,16,18,20]
num=int(input("Enter the number to check : "))
for i in range(len(l1)):
    if l1[i]==num:
        print("The number is available in the list at index ",i)