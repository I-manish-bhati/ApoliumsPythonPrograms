angle1=int(input("Enter internal angle 1 = "))
angle2=int(input("Enter internal angle 2 = "))
angle3=int(input("Enter internal angle 3 = "))
tri=angle3+angle1+angle2
if tri==180:
    print('Triangle is valid')
else:
    print('Triangle is not valid')