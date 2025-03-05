# Lesson 36
def primeNumberChecker(number):
    ''' checks if a given number is prime or not'''
    counter=0
    prime=False
    for i in range(1, number+1):
        if number%i==0:
            counter+=1
    if counter==2:
        prime=True
    return prime 
def primeFactoring(num):
    '''prime factors a num'''
    factors=[]
    if primeNumberChecker(num):
        factors.append(1)
        factors.append(num)
    else: 
        for i in range(1,num+1):
            if num%i==0:
                factors.append(i)
    return factors
print(primeFactoring(36))
print(primeNumberChecker(7))