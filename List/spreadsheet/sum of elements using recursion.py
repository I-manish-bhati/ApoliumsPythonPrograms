def func(sum,l1,n):
    sum=sum+l1[n]
    if n==0:
        print("Sum of all elements in an array is :",sum)
    func(sum,l1,n-1)
l1=[1,2,3]
sum=0
n=len(l1)
func(sum,l1,n-1)