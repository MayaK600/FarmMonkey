# Lesson 4
plankSec1= input ("Enter planks for section 1: ")
plankSec2 = input ("Enter planks for section 2: ")
plankSec3=input ("Enter planks for section 3: ")
totalPlank= len(plankSec1)+len(plankSec2)+len(plankSec3)
paintRemain=totalPlank
counter=0
while paintRemain>=12:
    paintRemain-=12
    counter+=1
if paintRemain!=0:
    counter+=1
cost=counter*14.95
print (f"Number of cans needed: {totalPlank} \nNumber of can remaining: {paintRemain}\nCost:{cost} ")