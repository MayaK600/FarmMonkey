# Lesson 23
sum=0
numOfNums=0
i=float(input("Enter first number (enter -1 to stop): ") )
while i!=-1:
    sum+=i
    numOfNums+=1
    i=float(input("Enter nextNum: "))
avg = sum/numOfNums
print (f"The avg is: {avg}")