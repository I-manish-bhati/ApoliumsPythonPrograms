num=int(input("Enter the number : "))

while num!=1:
    sum=0
    while num>0:
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    num=sum
    if num<10 and num!=1:
        break
if num==1:
    print("The number is a happy number ")
else:
    print("The number is not a happy number ")
        
