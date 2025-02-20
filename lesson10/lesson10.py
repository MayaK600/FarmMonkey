# Lesson 10
firstNum= int(input ("First number: "))
secondNum= int(input ("Second number: "))
thirdNum= int(input ("Third number: "))
fourthNum = int(input ("Fourth number: "))
safe = True 
if (firstNum == 9 or firstNum==8) and (fourthNum==9 or fourthNum==8):
    if (secondNum==thirdNum):
        safe=False
if safe:
    print("Not telemarketer")
else: 
    print("telemarketer")
