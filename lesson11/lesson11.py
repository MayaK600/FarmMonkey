# Lesson 11
point = input()
point =point.split(' ')

#fixedPoint = []
#for value in point:
#   fixedPoint.append(int(value))
point = list(map(int, point)) 
#converts the number in the list into integers 
#but we cannot use the numbers if it is in map sso we turn it into a list 
print (point)
#variable unpacking 
x , y=point
if x>0:
    if y>0:
        print ("Quadrent 1")
    else:
        print ("Quadrent 4")
else: 
    if y>0:
         print("Quadrent 2")
    else:
        print ("Quadrent 3")