# Lesson 4
def sumFinder(num):
    if num ==0 or num ==1:
        return num
    else: 
        return num +sumFinder(num-1)

print (f"sum of numbers between 1 to 10 is: {sumFinder(10)}")
    