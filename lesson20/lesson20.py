# Lesson 20
num=int(input("num: "))
sum=0
for i in range (1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("Perfect Num")
else:
    print("Not perfect Num")