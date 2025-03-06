# Lesson 40
def primeCheck(number):
    counter=0
    for i in range(2,number):
        if number%i==0:
            counter+=1
    return counter==0

def primeNumList (N):
    primes=[]
    for i in range(2,N):
        if primeCheck(i):
            primes.append(i)
    return primes

print(primeNumList(int(input("Enter number: "))))

