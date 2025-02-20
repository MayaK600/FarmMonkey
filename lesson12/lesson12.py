# Lesson 12
angles = input()
angles = angles.split(' ')
angles = list(map(int, angles))
a,b,c=angles
if sum(angles)==180:
    if a==b==c:
        print ("Equilateral")
    elif a==b or b==c or c==a:
        print ("Isosceles")
    else: 
        print ("Scalene")
else: 
    print ("Not triangle")
