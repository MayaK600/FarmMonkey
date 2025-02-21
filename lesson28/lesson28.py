# Lesson 28
num=input("Num: ")
palindrom=True
i=1
while i<=len(num):
    if num[i-1]!=num[i*-1]:
        palindrom=False 
    i+=1
if palindrom: 
    print("It is a palindrom")
else:
    print("It is not a palindrom")