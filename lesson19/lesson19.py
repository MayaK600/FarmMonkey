# Lesson 19
prime =True 
i = int(input("i: "))
j=2
while j<i:
    if i%j==0:
        prime=False 
        break
    j+=1
if prime:
    print(f"{i} is a prime number")
else:
    print (f"{i} is not a prime number")