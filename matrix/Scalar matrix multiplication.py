l1=[[1,2,3],[4,5,6],[7,8,9]]
num=int(input("Enter the number : "))
for i in range(len(l1)):
    for j in range(len(l1[i])):
        l1[i][j]*=num     
print(l1)