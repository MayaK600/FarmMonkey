# Lesson 38
def palindromeCheck(number):
    
    return number==number[::-1]

num1=999
num2=999
palindrome=[]
while num2>99: 
    while num1>99:
        currentNum=num1*num2
        if palindromeCheck(str(currentNum)):
             palindrome.append(currentNum)
        num1-=1
    num1=num2-1
    num2-=1

print(f"largest palindrome is {max(palindrome)}")