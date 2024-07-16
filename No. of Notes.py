amount = int(input('Enter the amount : '))
amount1 = int(input('Enter the amount : '))
count500= int(amount/500)
print('500 = ',count500)
amount=amount%500
count200=int(amount/200)
print('200 = ',count200)
amount=amount%200
count100=int(amount/100)
print('100 = ',count100)
amount=amount%100
count50=int(amount/50)
print('50 = ',count50)
amount=amount%50
count20=int(amount/20)
print('20 = ',count20)
amount=amount%20
count10=int(amount/10)
print('10 = ',count10)
amount=amount%10
count5=int(amount/5)
print('5 = ',count5)

notes=(500,200,100,50,20,10,5)
for i in notes:
    count=int(amount1/i)
    print('Notes of ',i,' : ',count)
    amount1=amount1%i