# Lesson 23
loop =True
sum=0
numOfNums=0
i=input("Enter first number (enter x to stop): ").lower()
while loop:
    if i=='x':
        loop = False
        break
    else: 
        i=float(i)
         sum+=i
         numOfNums+=1
    i=float(input("Enter nextNum: "))
avg = sum/numOfNums
print (f"The avg is: {avg}")