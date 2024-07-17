amount1 = int(input('Enter the amount : '))
notes=(500,200,100,50,20,10,5)
for i in notes:
    count=int(amount1/i)
    print('Notes of ',i,' : ',count)
    amount1=amount1%i