# Lesson 26
def factorCount (number):
    '''determines the number of factors the argument has 
    Args:
        number: an integer needed to determine the number of its factors 
    Returns: 
        an integer, which is the total amount of factors the argument has
    '''
    for dividor in range (1,number+1):
        if number % dividor==0:
            counter+=1
    return counter

num= int(input("N: "))
for i in range(1,num+1):
    factorSize =factorCount(i)
    print (f"{i} has {factorSize} factors")
