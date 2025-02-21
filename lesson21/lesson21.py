# Lesson 21
N=int(input("N: "))
largestNum=1
largest=0
for i in range(1,N):
    counter =0
    for p in range(1,i+1):
         if i%p==0:
             counter+=1
    if counter>largest:
        largestNum=i
        largest=counter
print(f"Most amount of factors: {i}")