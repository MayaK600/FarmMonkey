# Lesson 28
def palindromCheck(num): 
    palindrom=True
    i=1
    while i<=len(num):
         if num[i-1]!=num[i*-1]:
             palindrom=False 
         i+=1   
    return palindrom 

number=palindromCheck((input("Enter number: ")))
if number:
    print("it is a palindrom")
else:
    print ("Not a palindrom")