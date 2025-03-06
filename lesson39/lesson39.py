# Lesson 39
def devisorChecker(num,div):
    return num%div==0

num=int(input("Enter number: "))
largestDiv=[]
for div in range(1,num):
    if devisorChecker(num,div):
        largestDiv.append(div)

print(f"largest divisor is {max(largestDiv)}")