num=int(input("Enter the number : "))
count=0
x=num
sum=0
while x>0:
    count+=1
    x=x//10
sq=count
x=num
for i in range(1,count+1):
    rem=x%10
    sum+=rem**sq
    x=x//10
    sq-=1
if sum==num:
    print("The given number is an Disarium number")
else:
    print("The given number is not an Disarium number")