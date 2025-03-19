# Lesson 43
#part one
def duplicateRemove(aList):
    result=[]
    
    for value in aList:
        if value not in result:
            result.append(value)
    return result
test=[1,2,3,1,2,3,2,3,5,5,7]
print (duplicateRemove(test))

#or
def duplicateRemove2(aList):
    return list(set(aList))

print (duplicateRemove2(test))


#part 2
def uniqueLetters(aList):
    #will contain strings
    result=set()
    for word in aList:
        tempSet = set(word)
        result= result | tempSet
        # the | line means union 
    return result
test = ["hello", "goodbye", "Maya"]
print (uniqueLetters(test))

#part 3
def i_count (aList):
    #the list will contain several sets 
    if aList:
        result = aList[0]
        for exmp_set in aList[1:]:
            result = result & exmp_set #& represents intersection 
    return len(result)

test = [{1,2,3},{3,4,1},{1,3,4}]
print (i_count(test))


