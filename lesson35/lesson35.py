# Lesson 35
def doubleRemover(listA):
    ''' Function will look over a list of integers and create a new list with those values 
    and have no double occur
    '''
    listA.split(",")
    listB=[]
    if len(listA)>1:
        for i in range(len(listA)):
            currentCharacter=listA[i]
            if currentCharacter not in listB:
                listB.append(currentCharacter)
    else:
        listB=listA
    return listB
    
print(doubleRemover("4,n,7,n,4,5"))
