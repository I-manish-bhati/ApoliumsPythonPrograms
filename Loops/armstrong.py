num=int(input("Enter the number : "))
x=num
cmp=num
sum,count=0,0
while x>0:
    count=count+1
    x=x/10
for i in range(1,count+1):
    y = cmp%10
    sum = sum + y**3
    cmp= cmp//10
if sum==num:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")


