# Lesson 25
Num=int(input("Num: "))
largest=0
while (Num%2==0):
    Num//=2
    largest=max(largest,2)
    print(2)
for i in range (3,Num+1):
    while (Num%i==0):
        print (i)
        Num//=i
        largest=max(largest,i)
    i+=2
print (f"largest prime: {largest}")

